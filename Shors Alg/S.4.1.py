#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:37:57 2024

@author: adria
"""

def gcd(a, b):
    while a != b :
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def is_coprime(a, N):
    """Determine if two numbers are coprime.

    Args:
        a (int): First number to check if is coprime with the other.
        N (int): Second number to check if is coprime with the other.

    Returns:
        bool: True if they are coprime numbers, False otherwise.
    """
    return gcd(a, N) == 1

def is_odd(r):
    """Determine if a number is odd.

    Args:
        r (int): Integer to check if is an odd number.

    Returns:
        bool: True if it is odd, False otherwise.
    """
    
    return not (r/2).is_integer()


def is_not_one(x, N):
    """Determine if x is not +- 1 modulo N.

    Args:
        N (int): Modulus of the equivalence.
        x (int): Integer to check if it is different from +-1 modulo N.

    Returns:
        bool: True if it is different, False otherwise.
    """

    return not (x%N == 1 or x%N == N-1)


print("3 and 12 are coprime numbers: ", is_coprime(3, 12))
print("5 is odd: ", is_odd(5))
print("4 is not one mod 5: ", is_not_one(4, 5))