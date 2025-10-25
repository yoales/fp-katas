"""
Tests for Kata 3: Basic reduce operation
"""

import pytest
from python_katas.kata3 import sum_numbers

def test_sum_numbers():
    """Test summing numbers in a list"""
    assert sum_numbers([1, 2, 3, 4]) == 10
    assert sum_numbers([0, 0, 0]) == 0

def test_sum_numbers_with_negative():
    """Test summing numbers including negative values"""
    assert sum_numbers([-1, -2, 3, 4]) == 4
    assert sum_numbers([-1, -2, -3]) == -6

def test_sum_numbers_single_element():
    """Test summing numbers with a single element"""
    assert sum_numbers([5]) == 5
    assert sum_numbers([-5]) == -5 