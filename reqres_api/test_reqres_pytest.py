import requests
import pytest

def test_get_user_with_id_2_check_status_code_equals_200():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200


def test_get_user_with_id_1_check_content_type_equals_json():
    response = requests.get("https://reqres.in/api/users/1")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_get_user_with_id_1_check_name_equals_leanne_graham():
    response = requests.get("https://reqres.in/api/users/2")
    response_body = response.json()
    assert response_body["data"]["first_name"] == "Janet"


def test_get_user_with_id_1_check_company_name_equals_romaguera_crona():
    response = requests.get("https://reqres.in/api/users/3")
    response_body = response.json()
    assert response_body["data"]["email"] == "emma.wong@reqres.in"


def test_get_all_users_check_number_of_users_equals_10():
    response = requests.get("https://reqres.in/api/users")
    response_body = response.json()
    assert response_body["total"] >= 10
   


