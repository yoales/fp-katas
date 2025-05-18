# Python Functional Programming Katas

A collection of 10 Python katas that cover various functional programming concepts, ordered by difficulty level.

## Project Structure

```
python_katas/
├── src/
│   └── python_katas/
│       ├── __init__.py
│       ├── kata1.py  # Basic map operation
│       ├── kata2.py  # Basic filter operation
│       ├── kata3.py  # Basic reduce operation
│       ├── kata4.py  # Lambda functions
│       ├── kata5.py  # Combining map and filter
│       ├── kata6.py  # List comprehensions
│       ├── kata7.py  # Higher-order functions
│       ├── kata8.py  # Function composition
│       ├── kata9.py  # Currying
│       └── kata10.py # Complex functional operations
├── tests/
│   ├── __init__.py
│   ├── test_kata1.py
│   ├── test_kata2.py
│   ├── test_kata3.py
│   ├── test_kata4.py
│   ├── test_kata5.py
│   ├── test_kata6.py
│   ├── test_kata7.py
│   ├── test_kata8.py
│   ├── test_kata9.py
│   └── test_kata10.py
├── pyproject.toml
└── README.md
```

## Installation

```bash
pip install -e .
pip install pytest
```

## Running Tests

```bash
pytest
```

## Katas Overview

1. **Kata 1**: Basic map operation - Double each number in a list
2. **Kata 2**: Basic filter operation - Filter even numbers
3. **Kata 3**: Basic reduce operation - Sum all numbers
4. **Kata 4**: Lambda functions - Square numbers
5. **Kata 5**: Combining map and filter - Double even numbers
6. **Kata 6**: List comprehensions - Create a list of squares
7. **Kata 7**: Higher-order functions - Apply function to list
8. **Kata 8**: Function composition - Chain operations
9. **Kata 9**: Currying - Create specialized functions
10. **Kata 10**: Complex functional operations - Combine multiple concepts 