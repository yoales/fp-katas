"""
Kata 4: Lambda functions
Difficulty: 4/10

Task: Create a function that takes a list of numbers and returns a list of their squares
using lambda functions
"""

from typing import List, Callable

def create_square_function() -> Callable[[int], int]:
    """
    Create a lambda function that squares a number.
    
    Returns:
        A function that takes a number and returns its square
    """
    return lambda x: x ** 2

def square_numbers(numbers: List[int]) -> List[int]:
    """
    Square each number in the input list using the lambda function.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of squared integers
    """
    square_func = create_square_function()
    
    return list(map(square_func ,numbers))
    # Method signature: map(function, iterable) -> map object
    # TODO: Implement the function