"""
The data_upload module, responsible for dataset/data management and labeling.
"""

import datetime
from flask_restful import Resource, reqparse
import werkzeug
from database import users, images
from json_encode import json_encode


class ImageUpload(Resource):
    """ Upload image datasets. """
    def post(self, image_name, user_name):
        """
        Save an image (form data) associated with an user to ./images.

        :param image_name: an unique image_name
        :param user_name: the image's associated user, i.e. who uploaded the image
        :returns: the newly added image's information
        """
        parser = reqparse.RequestParser()
        parser.add_argument('file',
                            type=werkzeug.datastructures.FileStorage,
                            location='files',
                            required=True)
        args = parser.parse_args()
        image = args['file']
        image.save(f'./images/{image_name}.png')

        if users.find_one({'user_name': user_name}) is None:
            return {'ERROR': f'User {user_name} does not exist!'}, 400
        
        if images.find_one({'image_name': image_name}) is not None:
            return {'ERROR': 'image_name is NOT unique!'}, 400

        images.insert_one({'image_name': image_name,
                           'user_name': user_name,
                           'image_path': './images',
                           'image_type': '',
                           'image_classes': '',
                           'date_uploaded': datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')})
        return json_encode(images.find_one({'image_name': image_name})), 200
