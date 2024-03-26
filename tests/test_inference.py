"""
Test valid and invalid CRUD operations on TrainingAPI resource.
"""


import time
import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.reset import reset


inference_url = 'http://127.0.0.1:5000/model/inference'
files = {'file':open(os.path.join(os.path.dirname(__file__),
                                  'test_banana.jpeg'),
                                  'rb')}

def test_init():
    reset()


def test_create_inference_request():
    # assuming user and model are already created

    params = {'user_name':'testName',
              'model_name':'testModel',
              'inference_id':'testInference'}
    
    response = requests.post(url=inference_url,
                             params=params,
                             files=files)
    
    print(response.text)

    assert response.status_code == 201 # created


def test_get_inference_result():
    time.sleep(5) # wait for the queue to process the data and populate the database
    params = {'user_name':'testName',
              'inference_id':'testInference'}
    
    response = requests.get(url=inference_url,
                            params=params)
    
    print(response.text)

    assert response.status_code == 202 # accepted
