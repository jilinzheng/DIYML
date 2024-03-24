from pymongo import MongoClient
from database import *


def reset_db():
    users.delete_many({})
    images.delete_many({})
    models.delete_many({})


if __name__ == '__main__':
    reset_db()
