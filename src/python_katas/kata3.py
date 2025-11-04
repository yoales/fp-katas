"""
Kata 3: Basic reduce operation
Difficulty: 3/10

Task: Sum all numbers in a list using reduce
"""

from functools import reduce
from typing import List

def sum_numbers(numbers: List[int]) -> int:
    """
    Sum all numbers in the input list using reduce.
    
    Args:
        numbers: List of integers
        
    Returns:
        Sum of all integers
    """
    # Method signature: reduce(function, iterable[, initializer]) -> value
    return reduce(lambda acumul, nums: acumul + nums, numbers)
