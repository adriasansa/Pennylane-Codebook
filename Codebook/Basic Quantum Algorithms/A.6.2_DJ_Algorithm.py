#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:30:46 2024

@author: adria
"""

import numpy as np
import pennylane as qml

n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

def multisol_combo(n_bits, how_many):
    return np.random.randint(2, size=(how_many, n_bits))

def multisol_oracle_matrix(combos):
    """Return the oracle matrix for a set of solutions.

    Args:
        combos (list[list[int]]): A list of secret bit strings.

    Returns:
        array[float]: The matrix representation of the oracle.
    """
    indices = [np.ravel_multi_index(combo, [2]*len(combo)) for combo in combos] # Transforms from bit string to int!
    
    #My code
    
    my_array = np.identity(2**len(combos[0]))
    for i in range(len(indices)):
        index = indices[i]
        my_array[index, index] = -1
    return my_array

def multisol_hoh_circuit(combos):
    """A circuit which applies Hadamard, multi-solution oracle, then Hadamard.
    
    Args:
        combos (list[list[int]]): A list of secret bit strings.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """
    qml.broadcast(qml.Hadamard, wires = range(n_bits), pattern = "single")
    qml.QubitUnitary(multisol_oracle_matrix(combos), wires = range(n_bits))
    qml.broadcast(qml.Hadamard, wires = range(n_bits), pattern = "single")
    ##################
    # YOUR CODE HERE #
    ##################

    return qml.probs(wires=range(n_bits))

@qml.qnode(dev)
def deutsch_jozsa(promise_var):
    """Implement the Deutsch–Jozsa algorithm and guess the promise variable.
    
    Args:
        promise_var (int): Indicates whether the function is balanced (0) or constant (1).
        
    Returns: 
        int: A guess at the promise variable.
    """
    if promise_var == 0:
        how_many = 2**(n_bits - 1)
    else:
        how_many = np.random.choice([0, 2**n_bits]) # Choose all or nothing randomly
    combos = multisol_combo(n_bits, how_many) # Generate random combinations

    balanced = 0
    if np.isclose(multisol_hoh_circuit(combos)[0], 1):
            balanced = 1

    return balanced

print( deutsch_jozsa(0) )

print( deutsch_jozsa(1) )