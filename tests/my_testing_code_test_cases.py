# tests.py

import pytest
from scr.my_testing_code import add, subtract, multiply

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    with pytest.raises(ValueError):
        add(0, 1)

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, 1) == -2
    with pytest.raises(ValueError):
        subtract(0, 1)

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-1, 1) == -1
    with pytest.raises(ValueError):
        multiply(0, 1)