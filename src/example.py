"""This module provides an example of proper docstring format in Python.

This example contains a simple function to add two numbers together.

Attributes:
    None

Example:
    result = add_numbers(3, 5)
    print(result)  # Output: 8
"""

def add_numbers(a, b):
    """Add two numbers and return the result.

    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add.

    Returns:
        int, float: The sum of a and b.
    """
    return a + b


# Example usage:
if __name__ == '__main__':
    result = add_numbers(3, 5)
    print(result)  # Output: 8
