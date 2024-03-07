"""
Main application that uses all modules.
"""
import json
import datetime
from flask import Flask
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson import json_util
# from auth import Users

# set up flask/flask-restful
app = Flask(__name__)
api = Api(app)

# set up mongodb database
client = MongoClient("mongodb://localhost:27017/")
db = client["diyml_db"]
users = db["users"]
images = db["images"]
models = db["models"]

def json_encode(target):
    ''' json-encoding helper function for request return data '''
    return json.loads(json_util.dumps(target))

class UserAPI(Resource):
    ''' API for all user-related functions '''
    def get(self, user_name):
        ''' return user information '''
        return json_encode(users.find_one({"user_name": user_name}))

    def post(self, user_name, user_pass):
        ''' creates a new user, returning the new user [object] id '''
        users.insert_one({"user_name": user_name,
                          "user_pass": user_pass, 
                          "date_created": datetime.datetime.now().strftime("%Y/%m/%d")})
        return json_encode(users.find_one({"user_name": user_name}, 
                                          {"_id": 1}))


api.add_resource(UserAPI, '/user/<string:user_name>/<string:user_pass>')


if __name__ == '__main__':
    app.run(debug=True)
