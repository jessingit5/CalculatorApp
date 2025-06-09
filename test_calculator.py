import pytest

from calculator import add, substract, multiply, divide

def test_add():

    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_substract(): 
  
    assert substract(5, 3) == 2
    assert substract(2, 5) == -3

def test_multiply():

    assert multiply(2, 3) == 6
    assert multiply(-2, 4) == -8

def test_divide():

    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

    assert divide(0, 5) == 0
   
    with pytest.raises(ValueError):
        divide(1, 0)