# Python Functional Programming Katas

A collection of 10 Python katas that cover various functional programming concepts, ordered by difficulty level.

## About This Project

This repository is designed as a hands-on introduction to **functional programming in Python**. Each kata focuses on a specific concept, gradually increasing in complexity. The katas are ideal for self-study, coding dojos, or as exercises in programming courses.

The project encourages you to:
- Practice writing concise, expressive, and testable code.
- Learn and apply functional programming paradigms such as `map`, `filter`, `reduce`, lambdas, higher-order functions, currying, and function composition.
- Understand how to combine these concepts to solve more complex problems.

## Learning Objectives

By completing these katas, you will:
- Gain familiarity with Python’s functional programming tools.
- Improve your ability to write clean and modular code.
- Develop problem-solving skills using pure functions and immutable data.
- Learn to write and run unit tests with `pytest`.

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

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/)
- [pytest](https://docs.pytest.org/en/stable/)

### Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/yourusername/fp-katas.git
cd fp-katas
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install pytest
```

### Running Tests

Run all tests using `pytest`:

```bash
pytest
```

## Katas Overview

Each kata is a Python module with a specific functional programming challenge. Corresponding tests are provided in the `tests/` directory.

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

## Example Usage

Here’s how you might use one of the implemented katas in a Python shell:

```python
from python_katas.kata1 import double_numbers

print(double_numbers([1, 2, 3]))  # Output: [2, 4, 6]
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to add new katas, improve documentation, or enhance tests.
