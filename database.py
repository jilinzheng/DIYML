"""
MongoDB database running locally.
Collections: users, images, and models.
"""
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['diyml_db']
users = db['users']
images = db['images']
models = db['models']
