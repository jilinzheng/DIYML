"""
MongoDB database running locally.
Collections: users, images, and models.
"""


import os
from pymongo import MongoClient


MONGODB = os.environ.get('MONGODB','127.0.0.1')

# https://pymongo.readthedocs.io/en/stable/faq.html#using-pymongo-with-multiprocessing
def mongo_connect():
    """ Connect to MongoDB """
    client = MongoClient(f'mongodb://{MONGODB}:27017/')
    db = client['diyml_db']
    users = db['users']
    images = db['images']
    models = db['models']
    inferences = db['inferences']
    return users, images, models, inferences
