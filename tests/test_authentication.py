"""
Test valid and invalid CRUD operations on UserAPI resource.
"""


import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.reset_db import reset_db


url = 'http://localhost:5000/user'


def test_init():
    reset_db()


def test_create_user():
    params = {'user_name':'testName',
               'user_pass':'testPass'}
    response = requests.post(url=url,
                             params=params)
    assert response.status_code == 201 # created


def test_get_user():
    params = {'user_name':'testName'}
    response = requests.get(url=url,
                            params=params)
    assert response.status_code == 200 # ok


def test_update_user():
    params = {'user_name':'testName',
               'user_pass':'newPass'}
    response = requests.put(url=url,
                            params=params)
    assert response.status_code == 202 # accepted


def test_delete_user():
    params = {'user_name':'testName'}
    response = requests.delete(url=url,
                               params=params)
    assert response.status_code == 202 # accepted
