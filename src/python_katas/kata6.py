"""
Kata 6: List comprehensions
Difficulty: 6/10

Task: Create a function that uses list comprehension to generate a list of squares
and filter out negative numbers
"""

from typing import List

def square_positive_numbers(numbers: List[int]) -> List[int]:
    """
    Square positive numbers in the input list using list comprehension.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of squared positive integers
    """
    def filter_func(x):
        return x > 0
    def map_func(x):
        return x * x
    even_result = filter(filter_func, numbers)
    return list(map(map_func, even_result))