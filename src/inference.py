"""
Process inference requests.
"""


import os
import pickle
import json
from flask import jsonify
from flask_restful import Resource, reqparse
import werkzeug
from skimage.io import imread
from skimage.transform import resize
import numpy as np


class InferenceAPI(Resource):
    """ Process inference requests. """
    def post(self):
        """
        Send image file to be inferenced with selected user's selected model.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must specify an user.')
        parser.add_argument('model_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must provide a model name.')
        parser.add_argument('file',
                            type=werkzeug.datastructures.FileStorage,
                            location='files',
                            required=True,
                            help='You must provide at least one image!')
        args = parser.parse_args()

        user_name = args['user_name']
        model_name = args['model_name']
        file = args['file']

        model_location = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                               'models',
                               f'{user_name}')
        
        with open(os.path.join(model_location,
                               f'{model_name}.p'),
                               'rb') as f:
            model = pickle.load(f)

        file = imread(file)
        file = resize(file, (15, 15))
        file = file.flatten()

        prediction = model.predict([file])
        if prediction[0] == 0:
            return {'result':'apple'}, 202
        elif prediction[0] == 1:
            return {'result':'banana'}, 202
        elif prediction[0] == 2:
            return {'result':'grape'}, 202
        elif prediction[0] == 3:
            return {'result':'mango'}, 202
        elif prediction[0] == 4:
            return {'result':'strawberry'}, 202

        return json.dumps(prediction.tolist()), 202