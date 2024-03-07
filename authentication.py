"""
User authentication module.
"""

from flask_restful import Resource
from diyml import db

users = db["users"]

class UserAPI(Resource):
    ''' sample user api to figure out flask-restful. '''
    def get(self, user_name):
        ''' return user information '''
        return users.find_one({"user_name": user_name})

    def post(self, user_name, user_pass):
        ''' creates a new user, returning the new user information '''
        users.insert_one({"user_name": user_name, "user_pass": user_pass})
        return users.find_one({"user_name": user_name})
