#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:40:32 2024

@author: adria
"""

import numpy as np
import pennylane as qml

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)

def measure_in_y_basis():
    ##################
    # YOUR CODE HERE #
    ##################
    
    # PREPARE THE STATE
    prepare_psi()
    # PERFORM THE ROTATION BACK TO COMPUTATIONAL BASIS
    # y_basis_rotation()
    qml.adjoint( y_basis_rotation )()
    # RETURN THE MEASUREMENT OUTCOME PROBABILITIES

    return qml.probs(wires = 0)


# WRITE A QUANTUM FUNCTION THAT PREPARES (1/2)|0> + i(sqrt(3)/2)|1>
def prepare_psi():
    qml.StatePrep(np.array([1/2, np.sqrt(3)/2*1j]), wires=0)


# WRITE A QUANTUM FUNCTION THAT SENDS BOTH |0> TO |y_+> and |1> TO |y_->
def y_basis_rotation():
    qml.Hadamard(wires=0)
    qml.S(wires=0)


print(measure_in_y_basis())
