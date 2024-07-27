#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 22:18:35 2024

@author: adria
"""

import numpy as np

def coefficients_to_values(coefficients):
    """Returns the value representation of a polynomial
    
    Args:
        coefficients (array[complex]): a 1-D array of complex 
            coefficients of a polynomial with 
            index i representing the i-th degree coefficient

    Returns: 
        array[complex]: the value representation of the 
            polynomial 
    """

    return np.fft.fft(coefficients)

def values_to_coefficients(values):
    """Returns the coefficient representation of a polynomial
    
    Args:
        values (array[complex]): a 1-D complex array with 
            the value representation of a polynomial 

    Returns: 
        array[complex]: a 1-D complex array of coefficients
    """

    return np.fft.ifft(values)

def nearest_power_of_2(x):
    """Given an integer, return the nearest power of 2. 
    
    Args:
        x (int): a positive integer

    Returns: 
        int: the nearest power of 2 of x
    """
    
    return int(2**(np.ceil(np.log2(x))))

def fft_multiplication(poly_a, poly_b):
    """Returns the result of multiplying two polynomials
    
    Args:
        poly_a (array[complex]): 1-D array of coefficients 
        poly_b (array[complex]): 1-D array of coefficients 

    Returns: 
        array[complex]: complex coefficients of the product
            of the polynomials
    """
    ##################
    # YOUR CODE HERE #
    ################## 

    # Calculate the number of values required
    grade_a = np.size(poly_a) - 1 
    grade_b = np.size(poly_b) - 1 
    num_values = grade_a+grade_b + 1
    
    # Figure out the nearest power of 2
    dim = nearest_power_of_2(num_values)
    
    # Pad zeros to the polynomial
    poly_a_pad = np.pad(poly_a, pad_width= (0,dim-np.size(poly_a))) 
    poly_b_pad = np.pad(poly_b, pad_width= (0,dim-np.size(poly_b))) 
    
    # Convert the polynomials to value representation 
    val_a = coefficients_to_values(poly_a_pad)
    val_b = coefficients_to_values(poly_b_pad)
    
    # Multiply
    mul = val_a*val_b
    # Convert back to coefficient representation
    
    return values_to_coefficients(mul)

A = [1,1]
B = [1,-1]
print(fft_multiplication(A,B))