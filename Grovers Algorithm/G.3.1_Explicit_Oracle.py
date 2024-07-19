#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:52:31 2024

@author: adria
"""

import numpy as np
import pennylane as qml

n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qml.device("default.qubit", wires=all_wires)

def oracle(combo):
    """Implement an oracle using a multi-controlled X gate.

    Args:
        combo (list): A list of bits representing the secret combination.
    """
    combo_str = "".join(str(j) for j in combo)
    qml.MultiControlledX(query_register, aux, control_values = combo_str)
    pass  # APPLY MULTI-CONTROLLED X
    
def hadamard_transform(my_wires):
    """Apply the Hadamard transform on a given set of wires.

    Args:
        my_wires (list[int]): A list of wires on which the Hadamard transform will act.
    """
    for wire in my_wires:
        qml.Hadamard(wires=wire)


def diffusion():
    """Implement the diffusion operator using the Hadamard transform and
    multi-controlled X."""
    hadamard_transform(query_register)
    qml.MultiControlledX(query_register, aux, control_values = "".join("0" for j in query_register))
    hadamard_transform(query_register)
    ##################
    # YOUR CODE HERE #
    ##################
    pass

combo = (0,0,0,0,0)
@qml.qnode(dev)
def grover_circuit(combo):
    """Apply the MultiControlledX Grover operator and return probabilities on
    query register.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[float]: Measurement outcome probabilities.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    # PREPARE QUERY AND AUXILIARY SYSTEM
    hadamard_transform(query_register)
    qml.PauliX(wires = aux)
    qml.Hadamard(wires = aux)
    
    # APPLY GROVER ITERATION
    oracle(combo)
    diffusion()
    
    return qml.probs(wires=query_register)

print(grover_circuit(combo))