#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:07:40 2024

@author: adria
"""

# This code will only run directly on Pennylane's codebook!!!

dev = qml.device("default.qubit", wires=10)

def estimates_array(unitary):
    """ Given a unitary, return a list of its phase windows
    
    Args: 
        unitary (array[complex]): A unitary matrix.
    
    Returns:
        [(float, float)]: a list of phase windows for 2 to 9 
        estimation wires
    """

    estimates = []
    estimation_wires_loop = [range(0,i) for i in range(2, 10)]
    target_wires = [9]
    #print(estimation_wires_loop)
    for i in range( 8 ):
        estimation_wires = estimation_wires_loop[i]
        probs = qpe(unitary, estimation_wires, target_wires)
        estimates.append( phase_window(probs, estimation_wires) )

    return estimates

# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

estimates_array(U)

print(estimates_array(U))

###################
# SUBMIT FOR PLOT #
###################
