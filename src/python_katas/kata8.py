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
    # Method signature: compose(f, g)(x) = f(g(x))
    def inner(x):
        results = x
        for func in functions:
            results = func(results)
        return results
    
    return inner


def apply_composition(numbers: List[int]) -> List[int]:
    """
    Apply a composition of functions to a list of numbers.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of processed integers
    """

    double = lambda x: x * 2
    square = lambda x: x ** 2
    add_one = lambda x: x + 1

    # Method signature: map(function, iterable) -> map object
    return list(map(compose(double, square, add_one), numbers))