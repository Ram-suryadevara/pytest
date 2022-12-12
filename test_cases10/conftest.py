import pytest


@pytest.fixture
def data_abc():
    aa = 25
    bb = 35
    cc = 45
    return [aa, bb, cc]


@pytest.fixture
def supply_url():
    return "https://reqres.in/api"


