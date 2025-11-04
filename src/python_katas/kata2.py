"""
Kata 2: Basic filter operation
Difficulty: 2/10

Task: Filter even numbers from a list using filter
"""

def filter_even_numbers(numbers: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, numbers))
    """
    Filter even numbers from the input list using filter.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of even integers
    """
    # Method signature: filter(function, iterable) -> filter object
    # TODO: Implement the function