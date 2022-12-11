from pytest import mark
from pytest import fixture


# @fixture(scope="class")
# def connect_db():
#     print("The employee database connected")
#     yield
#     print("The employee database disconnected")


# @mark.fixture_example
# def test_emp1(connect_db):
#     print("This is first employee")


# @mark.fixture_example
# def test_emp2(connect_db):
#     print("This is second employee")


# @mark.fixture_example
# def test_emp3():
#     print("no need db for third employee")





@fixture(autouse=True)
def abc():
    return 10


def test_emp1():
    assert 10 == abc