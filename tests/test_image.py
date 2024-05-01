"""
Test valid and invalid CRUD operations on ImageUpload resource.
"""


import os
import sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.reset import reset


USER_URL = 'http://127.0.0.1:5000/user'
IMAGE_URL = 'http://127.0.0.1:5000/image'
files = {'file':open(os.path.join(os.path.dirname(__file__),
                                  'test_apple.png'),
                                  'rb')}


def test_init():
    """ Reset database """
    reset()


def test_create_upload():
    """ Upload an image """
    # first create a test user testName if it doesn't exist
    params = {'user_name':'testName',
              'user_pass':'testPass'}
    response = requests.get(url=USER_URL,
                            params=params)
    if response.status_code == 400:
        response = requests.post(url=USER_URL,
                                 params=params)
        assert response.status_code == 201 # created

    # then test the image uploading with the testName user
    params = {'user_name':'testName',
              'category':'apple'}
    response = requests.post(IMAGE_URL,
                             params=params,
                             files=files)
    assert response.status_code == 201 # created


def test_delete_upload():
    """ Delete an uploaded image """
    # delete the test image file
    params = {'user_name':'testName',
              'image_name':'test_apple.png'}
    response = requests.delete(url=IMAGE_URL,
                               params=params)
    assert response.status_code == 202 # accepted

    # also cleanup the test user created
    params = {'user_name':'testName'}
    response = requests.delete(USER_URL,
                               params=params)
    assert response.status_code == 202 # accepted


if __name__ == "__main__":
    choice = int(input("""
Select an option:
0. reset()
1. test_create_upload()
2. test_delete_upload()
"""))
    if choice == 0:
        reset()
    elif choice == 1:
        test_create_upload()
    elif choice == 2:
        test_delete_upload()
    else:
        print("Invalid choice, exiting.")
