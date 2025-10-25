"""
Tests for Kata 10: Complex functional operations
"""

import pytest
from python_katas.kata10 import process_numbers

def test_process_numbers():
    """Test processing numbers with multiple operations"""
    # Test case 1: All numbers are processed
    assert process_numbers([1, 2, 3, 4, 5]) == 55  # 1 + 4 + 9 + 16 + 25
    
    # Test case 2: Some numbers are filtered out
    assert process_numbers([-1, 2, -3, 4, 11]) == 20  # 4 + 16 (11² > 100)
    

def test_process_numbers_edge_cases():
    """Test edge cases for number processing"""
    # Test case 1: Numbers exactly at boundaries
    # assert process_numbers([0, 10, 11]) == 100  # 0 filtered, 10² = 100, 11² > 100
    
    # Test case 2: Mix of positive and negative numbers
    # assert process_numbers([-5, 5, -10, 10]) == 125  # 25 + 100 