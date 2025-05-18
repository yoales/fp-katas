"""
Tests for Kata 5: Combining map and filter
"""

import pytest
from python_katas.kata5 import double_even_numbers

def test_double_even_numbers():
    """Test doubling only even numbers in a list"""
    assert double_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 8, 12]
    assert double_even_numbers([0, 1, 2, 3]) == [0, 4]
    assert double_even_numbers([]) == []

def test_double_even_numbers_with_negative():
    """Test doubling even numbers including negative values"""
    assert double_even_numbers([-2, -1, 0, 1, 2]) == [-4, 0, 4]

def test_double_even_numbers_all_odd():
    """Test doubling even numbers from a list with only odd numbers"""
    assert double_even_numbers([1, 3, 5, 7]) == [] 