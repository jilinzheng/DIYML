"""
Test valid and invalid CRUD operations on InferenceAPI resource.
"""


import time
import os
import sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.reset import reset


INFERENCE_URL = 'http://127.0.0.1:5000/model/inference'
files = {'file':open(os.path.join(os.path.dirname(__file__),
                                  'test_mango.jpeg'),
                                  'rb')}

def test_init():
    """ Reset database """
    reset()


def test_create_inference_request():
    """ Create an inference request """
    # assuming user and model are already created

    params = {'user_name':'default',
              'model_name':'testModel',
              'inference_id':'testInference'}

    response = requests.post(url=INFERENCE_URL,
                             params=params,
                             files=files)

    print(response.text)

    assert response.status_code == 201 # created


def test_get_inference_result():
    """ Get an inference result """
    time.sleep(5) # wait for the queue to process the data and populate the database
    params = {'user_name':'default',
              'inference_id':'testInference'}

    response = requests.get(url=INFERENCE_URL,
                            params=params)

    print(response.text)

    assert response.status_code == 202 # accepted


if __name__ == "__main__":
    choice = int(input("""
Select an option:
0. reset()
1. test_create_inference_request()
2. test_get_inference_result()
"""))
    if choice == 0:
        reset()
    elif choice == 1:
        test_create_inference_request()
    elif choice == 2:
        test_get_inference_result()
    else:
        print("Invalid choice, exiting.")
