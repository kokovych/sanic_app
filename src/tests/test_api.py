import json

from src.constants import (
    EMPTY_ERROR, USER_SUCCESS_CREATION, ERR_MSG_UNIQUE_EMAIL)

USER_URL = '/api/user/'
TEST_USER_DATA = {
    "email": "test_01@email.com",
    "password": "Password123"
}
ERR_REQUIRED_FIELD = 'This field is required'


def test_register_user_empty_request(app_test):
    request, response = app_test.test_client.post(USER_URL)
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 400
    assert resp_data == EMPTY_ERROR


def test_register_user_success(app_test):
    request, response = app_test.test_client.post(
        USER_URL, data=json.dumps(TEST_USER_DATA))
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 201
    assert resp_data == USER_SUCCESS_CREATION


def test_register_user_bad_data(app_test):
    no_email_data = {'password': 'password123'}
    no_password_data = {"email": "test_02@email.com"}

    # try to register user without email
    request, response = app_test.test_client.post(
        USER_URL, data=json.dumps(no_email_data))
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 400
    assert resp_data.get('error').get('email') == ERR_REQUIRED_FIELD

    # try to register user without password
    request, response = app_test.test_client.post(
        USER_URL, data=json.dumps(no_password_data))
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 400
    assert resp_data.get('error').get('password') == ERR_REQUIRED_FIELD

    # try to register user with existing email
    # note: current config - user already in DB from
    # previous tests
    request, response = app_test.test_client.post(
        USER_URL, data=json.dumps(TEST_USER_DATA))
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 400
    assert resp_data.get('error').get('email') == ERR_MSG_UNIQUE_EMAIL

    # bad password(length):
    TEST_USER_DATA['email'] = "test_02@email.com"
    TEST_USER_DATA['password'] = 'pas12'
    request, response = app_test.test_client.post(
        USER_URL, data=json.dumps(TEST_USER_DATA))
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 400
    assert resp_data.get('error').get('password') == 'is too short'
