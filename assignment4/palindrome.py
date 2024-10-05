"""
Python Development II
Assignment 4 - Palindrome Validator
John O.
October 4, 2024

This program contains a function that validates whether an input string is a palindrome.

Usage:
Enter a string as the argument for the is_palindrome() function, and it will return
a Boolean value of True or False. A palindrome is a word or sentence that is the
same both backwards and forwards.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

from collections import deque

def is_palindrome(input_string):
    """
        Checks whether the string input is a palindrome.

        Parameters:
        input_string(str): The word or sentence that is entered as the argument.

        Returns:
        bool: True if 'input_string' is a palindrome, False if it is not.
    """
    #  Checks whether 'input_string' is a string
    if not isinstance(input_string, str):
        raise ValueError(f'{input_string} is not a string')  #  ValueError raised if 'input_string' is not a string

    #  'input_string' is converted to a deque
    char_deque = deque(input_string)  #  Contains the characters entered

    #  Checks whether an empty string is entered
    if not char_deque:
        return False  #  Returns False if is_palindrome() is called with an empty string

    #  Checks for single-character input
    if len(char_deque) == 1:
        return True