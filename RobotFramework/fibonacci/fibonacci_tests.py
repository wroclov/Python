import pytest
from Fibonacci import fibonacci

def test_zero():
    assert fibonacci(0) == []

@pytest.mark.parametrize("a ,expected", [
    (-7, []),
    (-999, []),
    (-1, [])
])
def test_negative(a, expected):
    assert fibonacci(a) == expected

err_msg = "Error: input must be an integer"

def test_string():
    assert fibonacci("cat_and_dog") == err_msg

def test_one():
    assert fibonacci(1) == [0]

def test_ten():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]