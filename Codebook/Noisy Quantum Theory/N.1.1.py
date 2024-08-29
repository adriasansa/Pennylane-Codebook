#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:50:47 2024

@author: adria
"""

import numpy as np

def build_density_matrix(state_1, state_2, p_1, p_2):
    """Build the density matrix for two randomly prepared states.
    
    Args:
        state_1 (array[complex]): A normalized quantum state vector
        state_2 (array[complex]): A second normalized quantum state vector
        p_1 (float): The probability of preparing state_1
        p_2 (float): The probability of preparing state_2
        
    Returns:
        (np.array([array[complex]])): The density matrix for the preparation.
    """
    
    projector_1 = np.outer(state_1, state_1.conj()) # Compute the outer product of state_1 with itself
    projector_2 = np.outer(state_2, state_2.conj()) # Compute the outer product of state_2 with itself    
    
    density_matrix = p_1*projector_1 + p_2*projector_2 # Build the density matrix
    
    return density_matrix

print("state_1 = |+y>, state_2 = |+x>, p_1 = 0.5, p_2 = 0.5")
print("density_matrix:")
print(build_density_matrix([1,1j]/np.sqrt(2), [1,1]/np.sqrt(2), 0.5, 0.5))   

