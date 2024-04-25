"""
Process inference requests.
"""


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pickle
import json
from flask_restful import Resource, reqparse
import werkzeug
from skimage.io import imread
from skimage.transform import resize
from src import q
from src.database import mongo_connect
from src.utils.json_encode import json_encode


class InferenceAPI(Resource):
    """ Process inference requests. """
    def get(self):
        """
        Get an inference result.        
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must specify an user.')
        parser.add_argument('inference_id',
                            type=str,
                            location='args',
                            required=True,
                            help='You must provide an inference id.')
        args = parser.parse_args()

        user_name = args['user_name']
        inference_id = args['inference_id']
        args = parser.parse_args()

        inferences = mongo_connect()[3]

        return json_encode(inferences.find_one({'inference_id':inference_id})), 202

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
                            help='You must provide one image!')
        parser.add_argument('inference_id',
                            type=str,
                            location='args',
                            required=True,
                            help='You must provide an inference reference id.')
        args = parser.parse_args()

        user_name = args['user_name']
        model_name = args['model_name']
        file = args['file']
        inference_id = args['inference_id']

        save_location = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                     'uploads')
        file.save(os.path.join(save_location,
                               f'{file.filename}'))

        job = q.enqueue_call(func="worker.inference",
                             args=(user_name, model_name, file.filename, inference_id),
                             result_ttl=5000)
        
        return {'SUCCESS': f'Inference task {job.get_id()} added to task queue.'}, 201
