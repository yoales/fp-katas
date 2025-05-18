"""
Tests for Kata 7: Higher-order functions
"""

import pytest
from python_katas.kata7 import apply_function

def test_apply_function_with_numbers():
    """Test applying a function to numbers"""
    double = lambda x: x * 2
    assert apply_function(double, [1, 2, 3]) == [2, 4, 6]
    assert apply_function(double, []) == []

def test_apply_function_with_strings():
    """Test applying a function to strings"""
    upper = lambda x: x.upper()
    assert apply_function(upper, ['a', 'b', 'c']) == ['A', 'B', 'C']

def test_apply_function_with_custom_function():
    """Test applying a custom function"""
    def add_one(x):
        return x + 1
    assert apply_function(add_one, [1, 2, 3]) == [2, 3, 4] 