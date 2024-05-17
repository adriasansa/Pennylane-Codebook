#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:07:58 2024

@author: adria
"""

import numpy as np
import pennylane as qml

def entangle_qubits():
    ##################
    # YOUR CODE HERE #
    ##################

    # ENTANGLE THE SECOND QUBIT (WIRES=1) AND THE THIRD QUBIT
    
    qml.Hadamard(1)
    qml.CNOT([1,2])
    
def rotate_and_controls():
    ##################
    # YOUR CODE HERE #
    ##################

    # PERFORM THE BASIS ROTATION
    qml.CNOT([0,1])
    qml.Hadamard(0)
    # PERFORM THE CONTROLLED OPERATIONS
    qml.CNOT([1,2])
    qml.CZ([0,2])
    
def extract_qubit_state(input_state):
    """Extract the state of the third qubit from the combined state after teleportation.
    
    Args:
        input_state (array[complex]): A 3-qubit state of the form 
            (1/2)(|00> + |01> + |10> + |11>) (a|0> + b|1>)
            obtained from the teleportation protocol.
            
    Returns:
        array[complex]: The state vector np.array([a, b]) of the third qubit.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    full_state_ = input_state
    # DETERMINE THE STATE OF THE THIRD QUBIT
    return np.array([2*full_state_[0], 2*full_state_[-1]])
    
def state_preparation():
    qml.Hadamard(wires=0)

# Here is the teleportation routine for you
dev = qml.device("default.qubit", wires=3)

#################
# YOUR CODE HERE #
##################

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE


@qml.qnode(dev)
def teleportation():
    state_preparation()
    entangle_qubits()
    rotate_and_controls()    
    return qml.state()

# Print the extracted state after teleportation
full_state = teleportation()
print(extract_qubit_state(full_state))
