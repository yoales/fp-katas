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
    # Method signature: [expression for item in iterable if condition]
    # TODO: Implement the function
    mid_result = filter(lambda x: x>0, numbers)
    result = map(lambda x: x**2, mid_result)
    return list(result)