"""
Kata 7: Higher-order functions
Difficulty: 7/10

Task: Create a function that takes another function as an argument and applies it
to each element in a list
"""

from typing import List, Callable, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def apply_function(func: Callable[[T], R], items: List[T]) -> List[R]:
    """
    Apply a function to each element in the input list.
    
    Args:
        func: Function to apply to each element
        items: List of items to process
        
    Returns:
        List of processed items
    """
    return list(map(func, items))
    # Method signature: map(function, iterable) -> map object
    # TODO: Implement the function