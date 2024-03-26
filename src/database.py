"""
MongoDB database running locally.
Collections: users, images, and models.
"""


from pymongo import MongoClient


# https://pymongo.readthedocs.io/en/stable/faq.html#using-pymongo-with-multiprocessing
def mongo_connect():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['diyml_db']
    users = db['users']
    images = db['images']
    models = db['models']
    inferences = db['inferences']
    return users, images, models, inferences
