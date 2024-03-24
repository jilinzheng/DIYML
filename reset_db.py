from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['diyml_db']
users = db['users']
images = db['images']
models = db['models']


def reset_db():
    users.delete_many({})
    images.delete_many({})
    models.delete_many({})


if __name__ == '__main__':
    reset_db()
