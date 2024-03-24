"""
Test valid and invalid CRUD operations on TrainingAPI resource.
"""


import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.reset import reset


inference_url = 'http://localhost:5000/model/inference'
files = {'file':open(os.path.join(os.path.dirname(__file__),
                                  'test_banana.jpeg'),
                                  'rb')}

def test_init():
    reset()


def test_create_inference_request():
    # assuming user and model are already created

    params = {'user_name':'testName',
              'model_name':'testModel'}
    
    response = requests.post(url=inference_url,
                             params=params,
                             files=files)
    
    print(response.text)

    assert response.status_code == 202 # accepted