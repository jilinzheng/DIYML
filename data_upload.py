"""
Data uploading module, responsible for dataset/data management and labeling.
"""


import datetime
import os
from flask_restful import Resource, reqparse
import werkzeug
from database import users, images
from json_encode import json_encode


class ImageUpload(Resource):
    """ Upload image datasets. """
    def post(self):
        """
        Save an image (file) associated with an user to ./images.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must specify an user.')
        parser.add_argument('file',
                            type=werkzeug.datastructures.FileStorage,
                            location='files',
                            required=True,
                            help='You must provide at least one image!',
                            action='append')
        parser.add_argument('category',
                            type=str,
                            location='args',
                            required=True,
                            help='You must provide a category for each image!',
                            action='append')
        args = parser.parse_args()

        user_name = args['user_name']
        files = args['file']
        categories = args['category']

        if (len(files) != len(categories)):
            return {'ERROR': 'Each image must have exactly one category!'}, 400

        for ii, file in enumerate(files):
            file.save(f'./images/{file.filename}')

            if users.find_one({'user_name':user_name}) is None:
                return {'ERROR':f'{user_name} does not exist!'}, 400

            if images.find_one({'image_name':file.filename}) is not None:
                return {'ERROR':'image_name is NOT unique!'}, 400

            images.insert_one({'image_name':file.filename,
                               'user_name':user_name,
                               'image_path':f'./images/{file.filename}',
                               'image_category':categories[ii],
                               'date_uploaded':datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')}) # pylint: disable=line-too-long

        return json_encode(images.find_one({'image_name': file.filename})), 201

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

        if users.find_one({'user_name':user_name}) is None:
                return {'ERROR':f'{user_name} does not exist!'}, 400

        if images.find_one({'image_name':image_name}) is None:
            return {'ERROR':f'{image_name} does not exist!'}, 400
        
        os.remove(rf'C:\Users\Jilin\Desktop\DIYML\images\{image_name}')
        images.delete_one({'image_name':image_name})

        return {'SUCCESS': f'{image_name} has been deleted'}, 202