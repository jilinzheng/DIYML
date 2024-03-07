"""
Main application that uses all modules.
"""
from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
# from auth import Users

app = Flask(__name__)
api = Api(app)


client = MongoClient('localhost', 27017)
db = client.diyml_db
users = db.users
images = db.images
models = db.models


if __name__ == '__main__':
    app.run(debug=True)
