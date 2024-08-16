#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:49:44 2024

@author: adria
"""

import numpy as np
import pennylane as qml

dev = qml.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def U_power_2k(unitary, k):
    """ Computes U at a power of 2k (U^2^k)
    
    Args: 
        unitary (array[complex]): A unitary matrix
    
    Returns: 
        array[complex]: the unitary raised to the power of 2^k
    """
    ##################
    # YOUR CODE HERE #
    ##################  
    return np.linalg.matrix_power(unitary ,2**k)

def apply_controlled_powers_of_U(unitary):
    """A quantum function that applies the sequence of powers of U^2^k to
    the estimation wires.
    
    Args: 
        unitary (array [complex]): A unitary matrix
    """
    for i in estimation_wires:
        qml.ControlledQubitUnitary(U_power_2k(unitary, estimation_wires[-1]-i), i, target_wires)

    pass

def prepare_eigenvector():
    qml.PauliX(wires=target_wires)

@qml.qnode(dev)
def qpe(unitary):
    """ Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.
        
    Returns:
        array[float]: Measurement outcome probabilities on the estimation wires.
    """
    #Prepare target wire
    prepare_eigenvector()
    
    #Prepare superposition state
    for i in range(estimation_wires[-1]+1):
        qml.Hadamard(i)
        
    #Oracle
    apply_controlled_powers_of_U(unitary)

    #QFT-1
    qml.adjoint( qml.QFT(wires=estimation_wires) )

    return qml.probs(wires=estimation_wires)

def estimate_phase(probs):
    """Estimate the value of a phase given measurement outcome probabilities
    of the QPE routine.
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
    
    Returns:
        float: the estimated phase   
    """
    
    probs_round = [np.round(probs[i]) for i in range(len(probs))]
    probs_bin = '{0:03b}'.format(probs_round.index(1))
    phase = sum([ int(probs_bin[i])/2**(i+1) for i in np.arange(len(probs_bin))])
    return float(phase)

U = qml.T.compute_matrix()

probs = qpe(U)


estimated_phase = estimate_phase(probs)
print(estimated_phase)