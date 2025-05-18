"""
Tests for Kata 2: Basic filter operation
"""

import pytest
from python_katas.kata2 import filter_even_numbers

def test_filter_even_numbers():
    """Test filtering even numbers from a list"""
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([0, 1, 2, 3]) == [0, 2]
    assert filter_even_numbers([]) == []

def test_filter_even_numbers_with_negative():
    """Test filtering even numbers including negative values"""
    assert filter_even_numbers([-2, -1, 0, 1, 2]) == [-2, 0, 2]

def test_filter_even_numbers_all_odd():
    """Test filtering even numbers from a list with only odd numbers"""
    assert filter_even_numbers([1, 3, 5, 7]) == [] 