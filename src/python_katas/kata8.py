"""
Kata 8: Function composition
Difficulty: 8/10

Task: Create a function that composes multiple functions together
"""

from typing import List, Callable, TypeVar

T = TypeVar('T')

def compose(*functions: Callable[[T], T]) -> Callable[[T], T]:
    """
    Compose multiple functions together.
    
    Args:
        *functions: Functions to compose
        
    Returns:
        A function that applies all functions in sequence
    """
    def composed_function(x):
        for func in functions:
            x = func(x)
        return x
    return composed_function

def apply_composition(numbers: List[int]) -> List[int]:
    """
    Apply a composition of functions to a list of numbers.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of processed integers
    """

    def double_func(x):
        return x * 2

    def square_func(x):
        return x ** 2

    def add_one_func(x):
        return x + 1

    composed_func = compose(double_func, square_func, add_one_func)
    map_result = map(composed_func, numbers)
    return list(map_result)