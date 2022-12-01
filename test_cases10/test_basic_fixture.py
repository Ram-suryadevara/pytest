# pytest fixtures are functions that can create data, test doubles,
# or initialize system state for the test suite.
# Any test that wants to use a fixture
#   -must explicitly use this fixture function
"""as an argument to the test function, so dependencies are
  always stated up front:"""

# Fixtures for handling test dependencies, state, and reusable functionality
# Marks for categorizing tests and limiting access to external resources
# Parametrization for reducing duplicated code between tests
import pytest


# @pytest.fixture
# def supply_AA_BB_CC():
#     aa = 25
#     bb = 35
#     cc = 45
#     return [aa, bb, cc]


def test_comparewithAA(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[0] == zz, "aa and zz comparison failed"


def test_comparewithBB(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[1] == zz, "bb and zz comparison failed"


def test_comparewithCC(supply_AA_BB_CC):
    zz = 35
    assert supply_AA_BB_CC[2] == zz, "cc and zz comparison failed"


# pytest -k compare -v