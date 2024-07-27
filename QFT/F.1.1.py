#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 21:39:47 2024

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

def coefficients_to_values_manual_DFT(coefficients):
    """Returns the value representation of a polynomial
    
    Args:
        coefficients (array[complex]): a 1-D array of complex 
            coefficients of a polynomial with 
            index i representing the i-th degree coefficient

    Returns: 
        array[complex]: the value representation of the 
            polynomial 
    """
    dim = np.size(coefficients)
    x = [np.exp(2*np.pi*i*1j/(dim)) for i in range(dim)]
    y = np.zeros(dim, dtype=complex)
    for i in range(dim):
        for j in range(np.size(coefficients)):
            y[i] += coefficients[j]*x[i]**j
    ##################
    # YOUR CODE HERE #
    ################## 
    return y

A = [4, 3, 2, 1]
print(coefficients_to_values_manual_DFT(A))
print(coefficients_to_values(A))
