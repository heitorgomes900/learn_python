#!/usr/bin/env python3
#Copyright (c) 2008 Qtrac Ltd. All rights reserved.
"""
This module provides a few string manipulation funcions.

>>> is_balanced("(Python (is (not (lisp))))")
True
>>> shorten("The Crossing", 10)
'The Cro...'
>>> simplify(" some    text    with    spurious  whitespace   ")
'some text with spurious whitespace'
"""

import string

def shorten(text, lenght=25, indicator="..."):
    """ Returns text or a truncate copy with the indicator added

    text is any string; length is the maximum lenght of the returned
    string (including any indicator); indicator is the string added at
    the end to indicate that the text has been shortened

    >>> shorten("The Road")
    'The Road'
    >>> shorten("No Country for Old Men", 20)
    'No Country for Ol...'
    >>> shorten("Cities of the Plain", 15, "*")
    'Cities of the *'
    """ 
    if len(text) > lenght:
        text = text[:lenght - len(indicator)] + indicator
    return text

def simplify(text, whitespace=string.whitespace, delete=""):
    """Returns the text with multiple spaces reduced to single spaces
    
    The whitespace parameter is a string of characters, each of which
    is considered to be a space.
    If delete is not empty is should be a string, in which case any
    characters in the delete string are excluded from the resultant string.
    
    >>> simplify(" this    adn\n that\t too ")
    'this and that too'
    >>> simplify("  Washington   D.C.\n")
    'Washington D.C.'
    >>> simplify("  Washington   D.C.\n", delete=",;:.")
    'Washington DC'
    >>> simplify("  disemvoweled   ", delete="aeiou")
    'dsmvwld'
    """
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        result.append(word)
    return " ".join(result)

def is_balanced(text, brackets="()[]{}<>"):
    counts = {}
    left_for_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1
    return not any(counts.values())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
