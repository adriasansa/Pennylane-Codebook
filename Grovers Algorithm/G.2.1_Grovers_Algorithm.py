#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:27:56 2024

@author: adria
"""

import numpy as np
import pennylane as qml

n_bits = 5
dev = qml.device("default.qubit", wires=n_bits)

combo = [0]*n_bits

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

@qml.qnode(dev)
def grover_circuit(combo, num_steps):
    """Apply the Grover operator num_steps times to the uniform superposition
       and return the state.

    Args:
        combo (list[int]): A list of bits representing the secret combination.
        num_steps (int): The number of iterations of the Grover operator
            our circuit is to perform.

    Returns:
        array[complex]: The quantum state (amplitudes) after repeated Grover
        iterations.
    """
    qml.broadcast(qml.Hadamard, wires = range(n_bits), pattern = "single") # Uniform superposition
    
    for i in range(num_steps):
        qml.QubitUnitary(oracle_matrix(combo), wires = range(n_bits))
        qml.QubitUnitary(diffusion_matrix(), wires = range(n_bits))
    
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

print( grover_circuit(combo, 4) )