#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:59:45 2024

@author: adria
"""

# Some functions missing still for it to run!

import numpy as np

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

def shor(N):
    """Return the factorization of a given integer.

    Args:
       N (int): integer we want to factorize.

    Returns:
        array[int]: [p,q], the prime factors of N.
    """
    
    for a in np.arange(2, N-1):

        if is_coprime(a, N) == False:
            p = gcd(a,N)
            q = N/p
        else:
            r = get_period( get_matrix_a_mod_N(a, N), N)

            while is_odd(r) == False:
                x = a**(r/2)%N

                while (x != 1 or x != N-1):
                    p = gcd(x-1, N)
                    q = gcd(x+1, N)
                    return p, q


print(shor(21))
