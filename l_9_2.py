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

# WRITE A QUANTUM FUNCTION THAT PREPARES (1/2)|0> + i(sqrt(3)/2)|1>
def prepare_psi():
    qml.StatePrep(np.array([1/2, np.sqrt(3)/2*1j]), wires=0)
    return #qml.state()


# WRITE A QUANTUM FUNCTION THAT SENDS BOTH |0> TO |y_+> and |1> TO |y_->
def y_basis_rotation():
    qml.Hadamard(wires=0)
    qml.S(wires=0)
    return #qml.state() functions should not return any values!!!