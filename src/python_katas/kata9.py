"""
Kata 9: Complex functional operations
Difficulty: 9/10

Task: Create a function that combines multiple functional programming concepts
to process a list of numbers
"""

from functools import reduce
from typing import List, Callable, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def process_numbers(numbers: List[int]) -> int:
    """
    Process a list of numbers using multiple functional programming concepts.
    
    The function:
    1. Filters out negative numbers
    2. Squares the remaining numbers
    3. Filters out numbers greater than 100
    4. Sums the remaining numbers
    
    Args:
        numbers: List of integers
        
    Returns:
        Sum of processed numbers
    """
    def filter_pos(x):
        return x >= 0

    def map_square(x):
        return x * x

    def filter_less(x):
        return x <= 100
    
    def reduce_func(x, y):
        return x + y

    positive_numbers = filter(filter_pos, numbers)
    squared_numbers = map(map_square, positive_numbers)
    filtered_numbers = filter(filter_less, squared_numbers)
    total_sum = reduce(reduce_func, filtered_numbers)
    return total_sum