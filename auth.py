"""
User authentication module.
"""

from flask_restful import Resource, request
from flask_sqlalchemy import SQLAlchemy

class UsersAPI(Resource):
    ''' User Resource class. '''
    def get(self):
        '''
        Retrieve list of users for testing purposes.
        Will be deprecated after final implementation.
        '''
        users_list = []
        #for user in users.values():
        #    users_list.append(user['username'])
        return users_list

    def post(self):
        data = request.json
