#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:36:22 2024

@author: adria
"""

def nontrivial_square_root(m):
    """Return the first nontrivial square root modulo m.

    Args:
        m (int): modulus for which want to find the nontrivial square root

    Returns:
        int: the first nontrivial square root of m
    """
    x = 2
    cont = True
    while cont:
        if x**2 %m == 1:
            cont = False
        else:
            x += 1
            cont = True

    return x

print(nontrivial_square_root(391))

def gcd(a, b):
    while a != b :
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def factorization(N):
    """Return the factors of N.

    Args:
        N (int): number we want to factor.

    Returns:
        array[int]: [p,q] factors of N.
    """
    x = nontrivial_square_root(N)
    
    p = gcd(x-1, N)
    q = gcd(x+1, N)

    return p, q


N = 391
p, q = factorization(N)
print(f"{N} = {p} x {q}")
