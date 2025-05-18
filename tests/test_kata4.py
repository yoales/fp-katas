"""
Tests for Kata 4: Lambda functions
"""

import pytest
from python_katas.kata4 import create_square_function, square_numbers

def test_create_square_function():
    """Test creating a square function using lambda"""
    square_func = create_square_function()
    assert square_func(2) == 4
    assert square_func(3) == 9
    assert square_func(0) == 0
    assert square_func(-2) == 4

def test_square_numbers():
    """Test squaring numbers in a list"""
    assert square_numbers([1, 2, 3]) == [1, 4, 9]
    assert square_numbers([0, -1, 2]) == [0, 1, 4]
    assert square_numbers([]) == []

def test_square_numbers_with_negative():
    """Test squaring numbers including negative values"""
    assert square_numbers([-1, -2, -3]) == [1, 4, 9] 