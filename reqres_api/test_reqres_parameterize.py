import pytest
import requests
import json


test_data_users=[( 1,"George","Bluth"),(2, "Janet","Weaver"),(3, "Emma","Wong"),(4, "Eve", "Holt"),(5,"Charles","Morris")]

@pytest.mark.parametrize("userid, first_name, last_name", test_data_users)
def test_get_data_for_user_check_name(userid, first_name, last_name):
    response = requests.get(f"https://reqres.in/api/users/{userid}")
    response_body = response.json()
    assert response_body["data"]["first_name"] == first_name
    assert response_body["data"]["last_name"] == last_name


@pytest.fixture
def supply_url():
    return "https://reqres.in/api/login"


def test_login_valid(supply_url):

    data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
    url =supply_url
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text


def test_login_no_password(supply_url):
    url = supply_url
    data = {'email':'test@test.com'}
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text
    assert j['error'] == "Missing password", resp.text

def test_login_no_email(supply_url):
    url = supply_url
    data = {}
    resp = requests.post(url, data=data)
    print(resp.text)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text
    assert j['error'] == "Missing email or username", resp.text

