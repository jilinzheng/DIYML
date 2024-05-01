"""
Test valid and invalid CRUD operations on UserAPI resource.
"""


import os
import sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.reset import reset


URL = 'http://127.0.0.1:5000/user'


def test_init():
    """ Reset database """
    reset()


def test_create_user():
    """ Create an user """
    params = {'user_name':'testName',
               'user_pass':'testPass'}
    response = requests.post(url=URL,
                             params=params)
    print(response.content)
    assert response.status_code == 201 # created


def test_get_user():
    """ Retrieve user information """
    params = {'user_name':'testName'}
    response = requests.get(url=URL,
                            params=params)
    print(response.text)
    assert response.status_code == 200 # ok


def test_update_user():
    """ Update an user's password """
    params = {'user_name':'testName',
               'user_pass':'newPass'}
    response = requests.put(url=URL,
                            params=params)
    assert response.status_code == 202 # accepted


def test_delete_user():
    """ Delete an user """
    params = {'user_name':'testName'}
    response = requests.delete(url=URL,
                               params=params)
    assert response.status_code == 202 # accepted


if __name__ == "__main__":
    choice = input("""
Select an option:
0. reset()
1. test_create_user()
2. test_get_user()
3. test_update_user()
4. test_delete_user()
""")
    if choice == 0:
        reset()
    elif choice == 1:
        test_create_user()
    elif choice == 2:
        test_get_user()
    elif choice == 3:
        test_update_user()
    elif choice == 4:
        test_delete_user()
    else:
        print("Invalid choice, exiting.")
