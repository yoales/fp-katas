"""
Tests for Kata 1: Basic map operation
"""

import pytest
from python_katas.kata1 import double_numbers

def test_double_numbers():
    """Test doubling numbers in a list"""
    assert double_numbers([1, 2, 3]) == [2, 4, 6]
    assert double_numbers([0, -1, 5]) == [0, -2, 10]
    assert double_numbers([]) == []

def test_double_numbers_with_negative():
    """Test doubling numbers including negative values"""
    assert double_numbers([-1, -2, -3]) == [-2, -4, -6]

def test_double_numbers_with_zero():
    """Test doubling numbers including zero"""
    assert double_numbers([0, 1, 2]) == [0, 2, 4] 