import pytest


@pytest.mark.parametrize("input1, input2, output", [(5, 5, 25), (3, 5, 12)])
def test_add(input1, input2, output):
    assert input1*input2 == output, "failed"

# Let’s run the test by py.test -k test_add -v and see the result
