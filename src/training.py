"""
Contains TrainingAPI resource.
"""


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask_restful import Resource, reqparse
from src import q


class TrainingAPI(Resource):
    """ Preprocess data for training. """

    def post(self):
        """
        Produces an image classification model trained on requested categories.
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
        parser.add_argument('categories',
                            type=str,
                            required=True,
                            location='args',
                            help='You must specify categories to train on.',
                            action='append')
        args = parser.parse_args()

        user_name = args['user_name']
        model_name = args['model_name']
        categories = args['categories']

        job = q.enqueue_call(func="worker.train",
                             args=(user_name, model_name, categories),
                             result_ttl=5000)

        return {'SUCCESS': f'Model creation task {job.get_id()} added to task queue.'}, 201
