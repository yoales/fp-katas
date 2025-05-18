"""
Tests for Kata 9: Currying
"""

import pytest
from python_katas.kata9 import curry, create_multiplier, apply_multiplier

def test_curry():
    """Test currying a function"""
    add = lambda x, y: x + y
    curried_add = curry(add)
    add_five = curried_add(5)
    assert add_five(3) == 8
    assert add_five(10) == 15

def test_create_multiplier():
    """Test creating a multiplier function"""
    double = create_multiplier(2)
    assert double(4) == 8
    assert double(5) == 10

def test_apply_multiplier():
    """Test applying a multiplier to a list"""
    assert apply_multiplier([1, 2, 3], 2) == [2, 4, 6]
    assert apply_multiplier([1, 2, 3], 3) == [3, 6, 9]
    assert apply_multiplier([], 2) == []

def test_curry_with_different_types():
    """Test currying with different types"""
    concat = lambda x, y: str(x) + str(y)
    curried_concat = curry(concat)
    add_hello = curried_concat("Hello, ")
    assert add_hello("World") == "Hello, World" 