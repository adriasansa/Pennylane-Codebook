#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:25:10 2024

@author: adria
"""

import numpy as np
import pennylane as qml

dev = qml.device('default.mixed', wires = 2)

parity_even = 0.5*qml.PauliZ(wires=0) @ qml.PauliZ(wires=1)+ 0.5*qml.Identity(0) @ qml.Identity(1)
parity_odd = - 0.5*qml.PauliZ(wires=0) @ qml.PauliZ(wires=1)+ 0.5*qml.Identity(0) @ qml.Identity(1)

max_mixed = np.eye(4)/4
psi_plus = qml.math.dm_from_state_vector(np.array([1,0,0,1])/np.sqrt(2))

@qml.qnode(dev)
def parity_check_circuit(state,parity_operator):

    ################
    #YOUR CODE HERE#
    ################
    qml.QubitDensityMatrix(state, wires = [0,1])
    # PREPARE THE STATE

    # RETURN THE EXPECTATION VALUE OF THE PARITY OPERATOR
    return qml.expval(parity_operator)

print("Maximal mixed state expected values")
print(f"Odd Parity: {parity_check_circuit(max_mixed,parity_odd)}")
print(f"Even Parity: {parity_check_circuit(max_mixed,parity_even)}")

print("Maximal entangled state expected values")
print(f"Odd Parity: {parity_check_circuit(psi_plus,parity_odd)}")
print(f"Even Parity: {parity_check_circuit(psi_plus,parity_even)}")
