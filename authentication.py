"""
User authentication module.
"""

import datetime
from flask_restful import Resource
from json_encode import json_encode
from database import users


class UserAPI(Resource):
    """ API for all user-related functions """
    def get(self, user_name):
        """ 
        Gets user information.

        :param user_name: 
        :returns: all fields associated with an user document
        """
        return json_encode(users.find_one({'user_name': user_name}))

    def post(self, user_name, user_pass):
        """ 
        Creates a new user.
        
        :param user_name: an unique user_name
        :param user_pass: the new user's associated password
        :returns: the new user's ObjectID
        """
        if users.find_one({'user_name': user_name}) is not None:
            return {'ERROR': 'user_name is NOT unique!'}

        users.insert_one({'user_name': user_name,
                          'user_pass': user_pass, 
                          'date_created': datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')})
        return json_encode(users.find_one({'user_name': user_name},
                                          {'_id': 1}))

    def put(self, user_name, user_pass):
        """
        Update the user_pass associated with the user_name.

        :param user_name: user whose password shall be updated
        :param new_pass: the new password
        :returns: the modified user information
        """
        users.update_one({'user_name': user_name},
                         {'$set': {'user_pass': user_pass}})
        return json_encode(users.find_one({'user_name': user_name}))

    def delete(self, user_name):
        """
        Delete a specified user.
        
        :param user_name: user to be deleted
        """
        users.delete_one({'user_name': user_name})
        return json_encode(users.find_one({'user_name': user_name}))
