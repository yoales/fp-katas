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
    # Method signatures: filter(function, iterable) -> filter object, map(function, iterable) -> map object
    # TODO: Implement the function
    return list(map(
        lambda x: 2*x,
        filter(lambda x: x%2==0, numbers)
    ))