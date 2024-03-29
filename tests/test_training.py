"""
Test valid and invalid CRUD operations on TrainingAPI resource.
"""


import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.reset import reset


user_url = 'http://127.0.0.1:5000/user'
training_url = 'http://127.0.0.1:5000/model/training'


def test_init():
    reset()


def test_create_single_model():
    # first create a test user testName if it doesn't exist
    params = {'user_name':'testName',
              'user_pass':'testPass'}
    response = requests.get(url=user_url,
                            params=params)
    if response.status_code == 400:
        response = requests.post(url=user_url,
                                params=params)
        assert response.status_code == 201 # created
    
    # create model associated with user
    params = {'user_name':'testName',
              'model_name':'testModel',
              'categories':['Apple', 'Banana','Mango']}
    response = requests.post(url=training_url,
                             params=params)

    print(response.text)

    assert response.status_code == 201 # created

def test_create_multiple_models():
    # first create a test user testName if it doesn't exist
    params = {'user_name':'testName',
              'user_pass':'testPass'}
    response = requests.get(url=user_url,
                            params=params)
    if response.status_code == 400:
        response = requests.post(url=user_url,
                                params=params)
        assert response.status_code == 201 # created
    
    # create 10 models associated with user testName
    for ii in range(10):
        params = {'user_name':'testName',
                'model_name':f'testModel{ii}',
                'categories':['Apple', 'Banana','Mango']}
        response = requests.post(url=training_url,
                                params=params)
        print(response.text)
        assert response.status_code == 201 # created
 