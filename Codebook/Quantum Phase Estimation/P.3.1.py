#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:49:44 2024

@author: adria
"""

# This code will only run directly on Pennylane's codebook!!!

dev = qml.device("default.qubit", wires=10)

def fractional_binary_to_decimal(binary_fraction, wires):
    return float(binary_fraction/ 2 ** len(wires))

def phase_window(probs, estimation_wires):
    """ Given an array of probabilities, return the phase window of the 
    unitary's eigenvalue
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
        estimation_wires (list[int]): List of estimation wires
    
    Returns:
        (float, float): the lower and upper bound of the phase
    """
    ##################
    # YOUR CODE HERE #
    ##################
    probs = probs.tolist()
    bound_1_index = probs.index(max(probs))
    bound_1 = fractional_binary_to_decimal(bound_1_index, estimation_wires) # MOST LIKELY OUTCOME
    probs[bound_1_index] = 0
    
    bound_2_index = probs.index(max(probs))
    bound_2 = fractional_binary_to_decimal(bound_2_index, estimation_wires) # SECOND MOST LIKELY OUTCOME
    return (bound_1, bound_2)


# Test your solution

# You can increase the number of estimation wires to a maximum of range(0, 9)
estimation_wires = range(0, 7)

# The target is set to the last qubit
target_wires = [9]

# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

probs = qpe(U, estimation_wires, target_wires)
print(probs)

print(phase_window(probs, estimation_wires))

# MODIFY TO TRUE AFTER TESTING YOUR SOLUTION
done = True
