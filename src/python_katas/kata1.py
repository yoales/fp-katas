"""
Kata 1: Basic map operation
Difficulty: 1/10

Task: Double each number in a list using map
"""

def double_numbers(numbers: list[int]) -> list[int]:
    """
    Double each number in the input list using map.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of doubled integers
    """
    # Method signature: map(function, iterable) -> map object
    # TODO: Implement the function
    result = map(lambda x: x*2, numbers)
    return list(result)