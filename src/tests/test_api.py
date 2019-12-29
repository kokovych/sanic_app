import json

from src.constants import (EMPTY_ERROR, USER_SUCCESS_CREATION)

USER_URL = '/api/user/'
TEST_USER_DATA = {
    "email": "test_01@email.com",
    "password": "Password123"
}


def test_create_user_empty_request(app_test):
    request, response = app_test.test_client.post(USER_URL)
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 400
    assert resp_data == EMPTY_ERROR


def test_create_user_success(app_test):
    request, response = app_test.test_client.post(
        USER_URL, data=json.dumps(TEST_USER_DATA))
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 201
    assert resp_data == USER_SUCCESS_CREATION

