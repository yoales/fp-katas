"""
Tests for Kata 6: List comprehensions
"""

import pytest
from python_katas.kata6 import square_positive_numbers

def test_square_positive_numbers():
    """Test squaring positive numbers using list comprehension"""
    assert square_positive_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert square_positive_numbers([-1, 2, -3, 4]) == [4, 16]
    assert square_positive_numbers([]) == []

def test_square_positive_numbers_all_negative():
    """Test squaring numbers with all negative values"""
    assert square_positive_numbers([-1, -2, -3]) == []

def test_square_positive_numbers_with_zero():
    """Test squaring numbers including zero"""
    assert square_positive_numbers([0, 1, 2, 3]) == [1, 4, 9] 