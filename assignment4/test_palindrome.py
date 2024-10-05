"""
Python Development II
Assignment 4 - Palindrome Validator
Test Suite for palindrome.py module
John O.
October 5, 2024

This test suite ensures that the function, is_palindrome() in the module, palindrome.py, works correctly. It
verifies that the function returns False if the input string is not a palindrome and True for a wide range
of input, not just specific palindromes. It also verifies that a ValueError is raised with input that is
not a string.

Usage:
Run this test module using pytest.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

import palindrome
import pytest

from palindrome import is_palindrome


#  Verifies that ValueError is raised for non-string input
def test_non_string():
    with pytest.raises(ValueError):
        palindrome.is_palindrome(3.14)  #  This should raise a ValueError

#  Tests if is_palindrome() returns False when called with an empty string
def test_empty_string():
    assert palindrome.is_palindrome('') == False  #  Should return False when input is an empty string

#  Tests if is_palindrome() returns True if called with "a"
def test_input_is_a():
    assert is_palindrome('a') == True  #  Should return True for single-character input

#  Tests if is_palindrome() returns True if called with 'bb'
def test_input_bb():
    assert is_palindrome('bb') == True  #  Should return True when two characters are entered and are the same

#  Tests if is_palindrome() returns False if called with 'abc'
def test_input_abc():
    assert is_palindrome('abc') == False  #  Should return False when first and last characters are not the same

#  Tests if is_palindrome() returns True if called with 'laval'
def test_input_laval():
    assert is_palindrome('laval') == True  #  Should return True if called with 'laval'

#  Tests if is_palindrome() returns False if called with 'toronto'
def test_input_toronto():
    assert is_palindrome('toronto') == False  #  Should return False if called with 'toronto'