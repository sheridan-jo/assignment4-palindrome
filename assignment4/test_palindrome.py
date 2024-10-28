"""
Python Development II
Assignment 4 - Palindrome Validator
Test Suite for palindrome.py module
John O.
October 5, 2024

This test suite ensures that the function, is_palindrome()
in the module, palindrome.py, works correctly. It
verifies that the function returns False if the input
string is not a palindrome and True for a wide range
of input, not just specific palindromes. It also
verifies that a ValueError is raised with input that is
not a string.

Usage:
Run this test module using pytest.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

import pytest
import palindrome


from palindrome import is_palindrome



def test_non_string():
    """Test that a ValueError is raised for non-string input."""
    with pytest.raises(ValueError):
        palindrome.is_palindrome(3.14)

def test_empty_string():
    """Test that an empty string returns False."""
    assert palindrome.is_palindrome('') is False

def test_input_is_a():
    """Test that a single character returns True."""
    assert is_palindrome('a') is True

def test_input_bb():
    """Test that a two-character palindrome returns True."""
    assert is_palindrome('bb') is True

def test_input_abc():
    """Test that a non-palindrome string returns False."""
    assert is_palindrome('abc') is False

def test_input_laval():
    """Test that a multi-character palindrome returns True."""
    assert is_palindrome('laval') is True

def test_input_toronto():
    """Test that a non-palindrome city name returns False."""
    assert is_palindrome('toronto') is False

def test_input_with_sentence():
    """Test that a palindrome sentence with mixed cases and punctuation returns True."""
    assert is_palindrome('Able was I ere I saw Elba.') is True
