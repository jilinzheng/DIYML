"""
User module.
"""


import datetime
from flask_restful import Resource, reqparse
from .utils.json_encode import json_encode
from .database import mongo_connect


def init_parser(require_pass=False):
    """
    Initialize request parser.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('user_name',
                        type=str,
                        location='args',
                        required=True,
                        help='You must specify a user_name.')
    
    if require_pass:
        parser.add_argument('user_pass',
                            type=str,
                            location='args',
                            required=True,
                            help='You must specify a password for the user.')

    return parser


class UserAPI(Resource):
    """ API for all user-related functions """
    def get(self):
        """ 
        Gets user information.
        """
        parser = init_parser(require_pass=False)
        args = parser.parse_args()
        user_name = args['user_name']

        [users, images, models] = mongo_connect()

        if users.find_one({'user_name': user_name}) is None:
            return {'ERROR': f'{user_name} does not exist!'}, 400

        return json_encode(users.find_one({'user_name': user_name})), 200

    def post(self):
        """ 
        Creates a new user.
        """
        parser = init_parser(require_pass=True)
        args = parser.parse_args()
        user_name = args['user_name']
        user_pass = args['user_pass']

        [users, images, models] = mongo_connect()

        if users.find_one({'user_name': user_name}) is not None:
            return {'ERROR': f'{user_name} is NOT unique!'}, 400

        users.insert_one({'user_name': user_name,
                          'user_pass': user_pass, 
                          'date_created': datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')}) # pylint: disable=line-too-long

        return json_encode(users.find_one({'user_name': user_name})), 201

    def put(self):
        """
        Update the user_pass associated with the user_name.
        """
        parser = init_parser(require_pass=True)
        args = parser.parse_args()
        user_name = args['user_name']
        user_pass = args['user_pass']

        [users, images, models] = mongo_connect()

        if users.find_one({'user_name': user_name}) is None:
            return {'ERROR': f'{user_name} does not exist!'}, 400

        users.update_one({'user_name': user_name},
                         {'$set': {'user_pass': user_pass}})

        return json_encode(users.find_one({'user_name': user_name})), 202

    def delete(self):
        """
        Delete a specified user.
        """
        parser = init_parser(require_pass=False)
        args = parser.parse_args()
        user_name = args['user_name']

        [users, images, models] = mongo_connect()

        if users.find_one({'user_name': user_name}) is None:
            return {'ERROR': f'{user_name} does not exist!'}, 400

        users.delete_one({'user_name': user_name})

        return {'SUCCESS': f'{user_name} has been deleted'}, 202
