from os import path, remove
import shutil
from src.utils.database import *


def reset():
    users.delete_many({})
    images.delete_many({})
    models.delete_many({})
    test_path = path.join(path.dirname(path.dirname(path.dirname(__file__))),
                'images',
                'testName')
    if path.exists(test_path):
        shutil.rmtree(test_path)


if __name__ == '__main__':
    reset()
