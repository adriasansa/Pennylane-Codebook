#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:03:40 2024

@author: adria
"""
import numpy as np

def has_trace_one(matrix):
    """Check whether a matrix has unit trace.
    
    Args:
        matrix: (array(array[complex]))
    Returns:
        bool: True if the trace of matrix is 1, False otherwise
    """
    trace = 0
    for i in np.arange( np.shape(matrix)[0] ):
        trace += matrix[i][i]
    ##################
    # YOUR CODE HERE #
    ################## 
    
    return bool( trace == 1 )

matrix_1 = [[1/2,1j],[-1j,1/2]]
matrix_2 = [[1,2],[3,4]]
    
print("Does [[1/2,1j],[-1j,1/2]] have unit trace?")
print(has_trace_one(matrix_1))
print("Does [[1,2],[3,4]] have unit trace?")
print(has_trace_one(matrix_2))