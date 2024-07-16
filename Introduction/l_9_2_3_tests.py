#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:25:54 2024

@author: adria
"""
import numpy as np
import pennylane as qml


dev = qml.device("default.qubit", wires=1)
@qml.qnode(dev)

def circuit():
    prepare_psi()
    # H()
    qml.adjoint(H)()
    # qml.adjoint( qml.Hadamard(wires=0) )
    return qml.probs(wires=0)

def prepare_psi():
    qml.StatePrep(np.array([np.sqrt(1/2), -np.sqrt(1/2)]), wires=0)

def H():
    qml.Hadamard(wires = 0)
    # return qml.probs(wires=[0, 1])

print(circuit())