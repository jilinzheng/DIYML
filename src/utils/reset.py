"""
Reset MongoDB database and image directory.
"""


from os import path
import shutil
from src.database import mongo_connect


def reset():
    """ Reset database """
    [users, images, models, inferences] = mongo_connect()

    users.delete_many({})
    images.delete_many({})
    models.delete_many({})
    inferences.delete_many({})
    test_path = path.join(path.dirname(path.dirname(path.dirname(__file__))),
                'images',
                'testName')
    if path.exists(test_path):
        shutil.rmtree(test_path)


if __name__ == '__main__':
    reset()
