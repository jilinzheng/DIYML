"""
Test valid and invalid CRUD operations on TrainingAPI resource.
"""


import os
import sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.reset import reset


USER_URL = 'http://127.0.0.1:5000/user'
TRAINING_URL = 'http://127.0.0.1:5000/model/training'


def test_init():
    """ Reset database """
    reset()


def test_create_single_model():
    """ Create a model """
    # first create a test user testName if it doesn't exist
    params = {'user_name':'testName',
              'user_pass':'testPass'}
    response = requests.get(url=USER_URL,
                            params=params)
    if response.status_code == 400:
        response = requests.post(url=USER_URL,
                                params=params)
    assert response.status_code == 200 # created

    # create model associated with user
    params = {'user_name':'default',
              'model_name':'testModel',
              'categories':['Apple', 'Banana','Mango']}
    response = requests.post(url=TRAINING_URL,
                             params=params)

    print(response.text)

    assert response.status_code == 201 # created

def test_create_multiple_models():
    """ Create several models """
    # first create a test user testName if it doesn't exist
    params = {'user_name':'default',
              'user_pass':'testPass'}
    response = requests.get(url=USER_URL,
                            params=params)
    if response.status_code == 400:
        response = requests.post(url=USER_URL,
                                params=params)
        assert response.status_code == 201 # created

    # create 10 models associated with user testName
    for ii in range(10):
        params = {'user_name':'default',
                'model_name':f'testModel{ii}',
                'categories':['Apple', 'Banana','Mango']}
        response = requests.post(url=TRAINING_URL,
                                params=params)
        print(response.text)
        assert response.status_code == 201 # created


if __name__ == "__main__":
    choice = int(input("""
Select an option:
0. reset()
1. test_create_single_model()
2. test_create_multiple_models()
"""))
    if choice == 0:
        reset()
    elif choice == 1:
        test_create_single_model()
    elif choice == 2:
        test_create_multiple_models()
    else:
        print("Invalid choice, exiting.")
