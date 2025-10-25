"""
Kata 9: Currying
Difficulty: 9/10

Task: Create a function that demonstrates currying by creating specialized
functions from a general function
"""

from typing import Callable, TypeVar, List

T = TypeVar('T')
R = TypeVar('R')

def curry(func: Callable[[T, T], R]) -> Callable[[T], Callable[[T], R]]:
    """
    Curry a function that takes two arguments.
    
    Args:
        func: Function to curry
        
    Returns:
        Curried function that takes one argument at a time
    """
    # Method signature: curry(f)(x)(y) = f(x, y)
    # TODO: Implement the function

def create_multiplier(factor: int) -> Callable[[int], int]:
    """
    Create a function that multiplies its input by a factor.
    
    Args:
        factor: Number to multiply by
        
    Returns:
        Function that multiplies its input by the factor
    """
    # TODO: Implement the function

def apply_multiplier(numbers: List[int], factor: int) -> List[int]:
    """
    Apply a multiplier to each number in the list.
    
    Args:
        numbers: List of integers
        factor: Number to multiply by
        
    Returns:
        List of multiplied integers
    """
    # Method signature: map(function, iterable) -> map object
    # TODO: Implement the function