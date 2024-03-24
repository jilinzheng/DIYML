"""
Data uploading module, responsible for dataset/data management and labeling.
"""


import datetime
import os
from flask_restful import Resource, reqparse
import werkzeug
from .utils.database import images
from .utils.json_encode import json_encode


class ImageAPI(Resource):
    """ API for all image-related functions. """
    def post(self):
        """
        Save an image (file) associated with an user to ./images/{user_name}/{category}/{file.filename}.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must specify an user.')
        parser.add_argument('category',
                            type=str,
                            location='args',
                            required=True,
                            help='You must provide a category for each image!',)
        parser.add_argument('file',
                            type=werkzeug.datastructures.FileStorage,
                            location='files',
                            required=True,
                            help='You must provide at least one image!')
        args = parser.parse_args()

        user_name = args['user_name']
        category = args['category']
        file = args['file']

        save_location = os.path.join(os.path.dirname(__file__),
                               'images',
                               f'{user_name}',
                               f'{category}',)
        if not os.path.exists(save_location):
             os.makedirs(save_location)

        file.save(os.path.join(save_location,
                               f'{file.filename}'))

        # allows multiple users to have same filenames,
        # but one user cannot have multiple files with the same name
        if images.find_one({'$and': [{'user_name':user_name},
                                     {'image_name':file.filename}]}) is not None:
            return {'ERROR':f'{file.filename} is NOT unique to {user_name}!'}, 400

        images.insert_one({'image_name':file.filename,
                           'user_name':user_name,
                           'image_path':save_location,
                           'image_category':category,
                           'date_uploaded':datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')}) # pylint: disable=line-too-long

        return json_encode(images.find_one({'$and': [{'user_name':user_name},
                                                     {'image_name':file.filename}]})), 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must specify an user whose image shall be deleted.',)
        parser.add_argument('image_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must specify an image to delete.')
        args = parser.parse_args()

        user_name = args['user_name']
        image_name = args['image_name']

        if images.find_one({'$and': [{'user_name':user_name},
                                     {'image_name':image_name}]}) is None:
            return {'ERROR':f'{image_name} and/or {user_name} does not exist!'}, 400
        
        os.remove(os.path.join(f'{images.find_one({'$and': [{'user_name':user_name},
                                                            {'image_name':image_name}]})['image_path']}', image_name))
        images.delete_one({'$and': [{'user_name':user_name},
                                    {'image_name':image_name}]})

        return {'SUCCESS': f'{image_name} has been deleted'}, 202
