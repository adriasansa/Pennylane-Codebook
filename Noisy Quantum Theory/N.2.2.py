#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:49:21 2024

@author: adria
"""

import numpy as np

def eigenprojectors(obs):
    
    """
    Args:
        obs (np.array([array[complex]])): A Hermitian operator representing a quantum observable.
        
    Returns:
        (np.array(array[array[complex]])): An array containing the eigenprojectors of the observable.
        Therefore, it is an array that contains matrices.
    """

    ################
    #YOUR CODE HERE#
    ################

    eigenvectors = np.linalg.eig(obs)# Use numpy's linalg to calculate the eigenvectors of obs
    
    projectors = [ np.outer(eigenvectors[i], eigenvectors[i].conj()) for i in np.arange(np.shape(obs)[0])]# Use list comprehension to build a list of eigenprojectors from the eigenvectors
    
    return projectors
