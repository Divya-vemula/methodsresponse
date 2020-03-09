# import packages


import pytest
import math

from factorial import factorial_function
def test_factorial_functionlity():
    print("inside test_factorial_functionality")

    assert factorial_function(0) == 1
    assert factorial_function(4) ==24

def test_class_library():
    print("inside test_class_library")

    for i in range (5):
        assert math.factorial(i) == factorial_function(i)

def test_negative_number():
    print("inside test_negative_number")

    with pytest.raises(AssertionError):
        factorial_function(-10)


