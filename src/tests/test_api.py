from src.constants import (EMPTY_ERROR, USER_SUCCESS_CREATION)

USER_URL = '/api/user/'


def test_index_returns_200(app_test):
    request, response = app_test.test_client.get('/')
    assert response.status == 200


def test_create_user_empty_request(app_test):
    request, response = app_test.test_client.post(USER_URL)
    resp_data = response.json
    status_code = response.status_code.value
    assert status_code == 400
    assert resp_data == EMPTY_ERROR


def test_drop_all_test_db(drop_test_db):
    print('All tables from test DB were dropped!')


