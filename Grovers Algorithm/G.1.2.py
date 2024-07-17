#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:27:56 2024

@author: adria
"""

import numpy as np
import pennylane as qml

n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)


def oracle_matrix(combo):
    """Return the oracle matrix for a secret combination.

    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        array[float]: The matrix representation of the oracle.
    """
    index = np.ravel_multi_index(combo, [2] * len(combo))  # Index of solution
    my_array = np.identity(2 ** len(combo))  # Create the identity matrix
    my_array[index, index] = -1
    return my_array

def diffusion_matrix():
    """Return the diffusion matrix.

    Returns:
        array[float]: The matrix representation of the diffusion operator.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    Dim = 2 ** len(combo)
    Identity = np.identity(Dim)
    Psi_Part = 1/Dim*np.ones( (Dim,Dim) )
    return 2*Psi_Part - Identity

combo = (0,0,0,0)

@qml.qnode(dev)
def difforacle_amp(combo):
    """Apply the oracle and diffusion matrix to the uniform superposition.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The quantum state (amplitudes) after applying the oracle
        and diffusion.
    """
    
    qml.broadcast(qml.Hadamard, wires = range(n_bits), pattern = "single")
    qml.QubitUnitary(oracle_matrix(combo), wires = range(n_bits))
    qml.QubitUnitary(diffusion_matrix(), wires = range(n_bits))
    
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()