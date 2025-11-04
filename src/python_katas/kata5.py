"""
Kata 5: Combining map and filter
Difficulty: 5/10

Task: Create a function that doubles only the even numbers in a list
by combining map and filter operations
"""

from typing import List

def double_even_numbers(numbers: List[int]) -> List[int]:
    """
    Double only the even numbers in the input list by combining map and filter.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of doubled even integers
    """
    def filter_func(x):
        return x%2==0
    def map_func(x):
        return x * 2
    even_result = filter(filter_func, numbers)
    return list(map(map_func, even_result))