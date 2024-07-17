#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:12:45 2024

@author: adria
"""

import numpy as np
import pennylane as qml

n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

combos = ((0,0,0,0),(1,1,1,1),(0,0,1,0))
# combos = np.random.randint(2, size=(3, n_bits))

def multisol_oracle_matrix(combos):
    """Return the oracle matrix for a set of solutions.

    Args:
        combos (list[list[int]]): A list of secret bit strings.

    Returns:
        array[float]: The matrix representation of the oracle.
    """
    indices = [np.ravel_multi_index(combo, [2]*len(combo)) for combo in combos] # Transforms from bit string to int!
    # print(indices)
    #My code
    
    my_array = np.identity(2**len(combos[0]))
    for i in range(len(indices)):
        # print(indices[i])
        index = indices[i]
        my_array[index, index] = -1
    return my_array

# print( multisol_oracle_matrix(combos) )

@qml.qnode(dev)
def multisol_pair_circuit(x_tilde, combos):
    """Implements the circuit for testing a pair of combinations labelled by x_tilde.
    
    Args:
        x_tilde (list[int]): An (n_bits - 1)-bit string labelling the pair to test.
        combos (list[list[int]]): A list of secret bit strings.

    Returns:
        array[float]: Probabilities on the last qubit.
    """
    for i in range(n_bits-1): # Initialize x_tilde part of state
        if x_tilde[i] == 1:
            qml.PauliX(wires=i)
            
    qml.Hadamard(wires =n_bits-1)

    qml.QubitUnitary(multisol_oracle_matrix(combos), wires = range(n_bits))
    
    qml.Hadamard(wires =n_bits-1)
    
    ##################
    # YOUR CODE HERE #
    ##################

    return qml.probs(wires=n_bits-1)

def parity_checker(combos):
    """Use multisol_pair_circuit to determine the parity of a solution set.

    Args:
        combos (list[list[int]]): A list of secret combinations.

    Returns: 
        int: The parity of the solution set.
    """
    parity = 0
    x_tilde_strs = [np.binary_repr(n, n_bits-1) for n in range(2**(n_bits-1))]
    x_tildes = [[int(s) for s in x_tilde_str] for x_tilde_str in x_tilde_strs]
    
    for x_tilde in x_tildes:
        if np.isclose(multisol_pair_circuit(x_tilde, combos)[1], 1):
            parity = parity ^ 1
        ##################
        # YOUR CODE HERE #
        ##################

        # IMPLEMENT PARITY COUNTING ALGORITHM
    
    return parity

print(parity_checker(combos))