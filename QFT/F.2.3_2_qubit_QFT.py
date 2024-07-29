#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:47:10 2024

@author: adria
"""

import numpy as np
import pennylane as qml

num_wires = 2
dev = qml.device("default.qubit", wires=num_wires)

N = 2**num_wires
omega = np.exp(2*np.pi*1j/N)
QFT_matrix = 1/np.sqrt(N)*np.array([[1,1,1,1],[1,omega, omega**2, omega**3],[1,omega**2, omega**4, omega**6],[1,omega**3, omega**6, omega**9]])

@qml.qnode(dev)
def two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using qml.QubitUnitary. 
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qml.BasisStatePreparation(bits, wires=[0, 1])
    
    qml.QubitUnitary(QFT_matrix, wires = [0,1])
    
    return qml.state()

@qml.qnode(dev)
def decompose_two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using elementary gates.
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qml.BasisStatePreparation(bits, wires=[0, 1])
    
    qml.Hadamard(wires = 0)
    qml.ctrl(qml.S, control=1)(wires=0)
    qml.Hadamard(wires = 1)
    qml.SWAP(wires = [0,1])
    
    return qml.state()

print(two_qubit_QFT(0))
print(decompose_two_qubit_QFT(0))

