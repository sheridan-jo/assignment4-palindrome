"""
Python Development II
Assignment 4 - Palindrome Validator
Test Suite for palindrome.py module
John O.
October 4, 2024

This test suite ensures that the function, is_palindrome() in the module, palindrome.py, works correctly. It
verifies that the function returns False if the input string is not a palindrome and true for a wide range
of input, not just specific palindromes. It also verifies that a ValueError is raised with input that is
not a string.

Usage:
Run this test module using pytest.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

import palindrome
import pytest

#  Verifies that ValueError is raised for non-string input
def test_non_string():
    with pytest.raises(ValueError):
        palindrome.is_palindrome(3.14)  #  This should raise a ValueError