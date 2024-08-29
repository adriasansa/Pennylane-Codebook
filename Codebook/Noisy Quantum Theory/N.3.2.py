#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:23:03 2024

@author: adria
"""

import numpy as np
import pennylane as qml

def composite_density_matrix(rho, sigma):
    """Build composite density matrix from two states.
    
    Args:
        rho: (np.array(array[complex]): The density matrix of the first input state
        sigma: (np.array(array[complex]): The density matrix of the second input state
        
    Returns:
        (np.array([array[complex]])): The density matrix for the composite system.
    """
    
    return np.kron(rho, sigma)

def create_entangled(alpha):

    """ Subcircuit that creates the entangled state
    Args:
        - alpha (float): angle parameterizing the subcircuit.
    """
    qml.RY(alpha, wires = 0)
    qml.CNOT(wires = [0,1])

dev = qml.device("default.qubit", wires=2) # Create your device

@qml.qnode(dev)
def reduced_entangled(alpha):

    """
    Function that prepares an entangled state and calculates the reduced density matrix 
    on the first wire.
    Args:
        - alpha (float): Angle parametrizing the entangled state
    Returns:
        (np.array(complex)): Reduce density matrix on the first wire
    """
    create_entangled(alpha)
    # Prepare the state using create_entangled
    
    return qml.density_matrix(wires=0)# Return the density matrix on wire = 0

alpha = np.pi/3

print("For alpha = pi/3, the reduced density matrix is {}".format(reduced_entangled(alpha)))


