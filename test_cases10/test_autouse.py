# `autouse=True` will be initiated first than the other fixtures of the same scope.

import pytest
 
vegetables = [] 
 
@pytest.fixture
def cauliflower(potato):
    vegetables.append('cauliflower')
 
@pytest.fixture
def potato():
    vegetables.append('potato')
 
@pytest.fixture(autouse=True)
def onion():
    vegetables.append('onion')
 
def test_vegetables_order(cauliflower, onion):
    assert vegetables == ['onion', 'potato', 'cauliflower']