#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:52:31 2024

@author: adria
"""

import numpy as np
import pennylane as qml

combo = (0,0,0,0,0)

def grover_iter(combo, num_steps):
    """Run Grover search for a given secret combination and a number of iterations.

    Args:
        combo (list[int]): The secret combination, represented as a list of bits.
        num_steps (int): The number of Grover iterations to perform.

    Returns:
        array[float]: Probability for observing different outcomes.
    """
    
    n_bits = len(combo)
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
    
    @qml.qnode(dev)
    def inner_circuit():
        ##################
        # YOUR CODE HERE #
        ##################
        # IMPLEMENT THE GROVER CIRCUIT
        hadamard_transform(query_register)
        qml.PauliX(wires = aux)
        qml.Hadamard(wires = aux)
        
        for i in range(num_steps):
            oracle(combo)
            diffusion()
        return qml.probs(wires=query_register)

    return inner_circuit()

print( grover_iter(combo, 1) )