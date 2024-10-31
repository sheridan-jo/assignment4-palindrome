"""
Python Development II
Assignment 4 - Palindrome Validator
John O.
October 5, 2024

This program contains a function that validates whether an input string is a palindrome.

Usage:
Enter a string as the argument for the is_palindrome() function, and it will return
a Boolean value of True or False. A palindrome is a word or sentence that is the
same both backwards and forwards.

Imports:
    deque: Used to store the characters entered into is_palindrome() function.
    re: Used to remove non-alphanumeric characters and replace them with an empty string
            so that they are not a source of mismatch.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

from collections import deque
import re

def is_palindrome(input_string):
    """
        Checks whether the string input is a palindrome.

        Parameters:
        input_string(str): The word or sentence that is entered as the argument.

        Returns:
        bool: True if 'input_string' is a palindrome, False if it is not.
    """

    #  Raises ValueError if input is not a string
    if not isinstance(input_string, str):
        raise ValueError(f'{input_string} is not a string')

    #  Removes non-alphanumeric characters
    #  Converts input to lower case
    input_string = re.sub(r'[^a-zA-Z0-9]', '', input_string.lower())

    #  'input_string' is converted to a deque
    char_deque = deque(input_string)  #  Contains the characters entered

    #  Checks whether an empty string is entered
    if not char_deque:
        return False  #  Returns False if is_palindrome() is called with an empty string

    #  Checks for single-character input
    if len(char_deque) == 1:
        return True

    #  Compares characters from the beginning and end of 'char_deque'
    #  In each iteration, the rightmost and leftmost characters are removed and compared
    while len(char_deque) >= 2:
        rightmost_char = char_deque.pop()  #  Rightmost character removed and retrieved
        leftmost_char = char_deque.popleft()  #  Leftmost character removed and retrieved

        #  Rightmost and leftmost characters are compared
        #  Returns false if at any point characters do not match
        if rightmost_char != leftmost_char:
            return False

    #  Function returns True if the loop has terminated with no mismatches
    return True
