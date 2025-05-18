"""
Tests for Kata 8: Function composition
"""

import pytest
from python_katas.kata8 import compose, apply_composition

def test_compose():
    """Test function composition"""
    double = lambda x: x * 2
    square = lambda x: x ** 2
    add_one = lambda x: x + 1
    
    composed = compose(double, square, add_one)
    assert composed(2) == 17  # (2 * 2) ** 2 + 1 = 17
    assert composed(3) == 37  # (3 * 2) ** 2 + 1 = 37

def test_apply_composition():
    """Test applying composed functions to a list"""
    assert apply_composition([1, 2, 3]) == [5, 17, 37]
    assert apply_composition([]) == []

def test_compose_single_function():
    """Test composing a single function"""
    double = lambda x: x * 2
    composed = compose(double)
    assert composed(5) == 10 