import pytest


@pytest.mark.set1
def test_file2_method1():
    x = 5
    y = 6
    assert x+1 == y, "test failed"
    assert x == y, "test failed because x=" + str(x) + " y=" + str(y)


@pytest.mark.set1
def test_file2_method2():
    x = 5
    y = 6
    assert x+1 == y, "test failed"


# Run py.test -m set1.This will run the methods test_file1_method1,
#  test_file2_method1, test_file2_method2.
# Running py.test -m set2 will run test_file1_method2.
