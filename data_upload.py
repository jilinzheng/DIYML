"""
Data uploading module, responsible for dataset/data management and labeling.
"""


import datetime
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
        parser.add_argument('user',
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
#        parser.add_argument('category',
#                            type=str,
#                            required=True,
#                            help='You must provide a category for each image!',
#                            action='append')
        args = parser.parse_args()

        user = args['user']
        files = args['file']
#        categories = args['categories']

#        if (len(files) != len(categories)):
#            return {'ERROR': 'Each image must have exactly one category!'}, 400

        for ii, file in enumerate(files):
            file.save(f'./images/{file.filename}')

            if users.find_one({'user_name': user}) is None:
                return {'ERROR': f'User {user} does not exist!'}, 400

            if images.find_one({'image_name': file.filename}) is not None:
                return {'ERROR': 'image_name is NOT unique!'}, 400

            images.insert_one({'image_name': file.filename,
                               'user_name': user,
                               'image_path': './images',
                               'image_type': '',
#                               'image_category': categories[ii],
                               'date_uploaded': datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')}) # pylint: disable=line-too-long

        return json_encode(images.find_one({'image_name': file.filename})), 200
