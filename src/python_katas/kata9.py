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
    return reduce(lambda x, y: x+y, filter(lambda x: x<=100, map(lambda x: x**2, filter(lambda x: x>=0, numbers))))
    # Method signatures: filter(function, iterable) -> filter object, map(function, iterable) -> map object, reduce(function, iterable[, initializer]) -> value
    
    # TODO: Implement the function