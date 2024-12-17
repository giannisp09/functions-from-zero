"""
A  calculator module
"""


def add(a, b):
    """
    Add two numbers
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers
    """
    return a / b


# build a function to calculate the factorial of a number
def factorial(n):
    """
    Calculate the factorial of a number
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
