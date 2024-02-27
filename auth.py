"""
User authentication module.
"""

from flask_restful import Resource

users = {
    0:{'username':'username', 'password':'password'},
    1:{'username':'jilin', 'password':'admin'},
    2:{'username':'jimbo', 'password':'jimboisreallycool'}
}

class Users(Resource):
    ''' User Resource class. '''
    def get(self):
        '''
        Retrieve list of users for testing purposes.
        Will be deprecated after final implementation.
        '''
        users_list = []
        for user in users.values():
            users_list.append(user['username'])
        return users_list
