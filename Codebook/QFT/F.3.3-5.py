#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:40:15 2024

@author: adria
"""

import numpy as np
import pennylane as qml

dev = qml.device('default.qubit', wires=4)

def swap_bits(n_qubits):
    """A circuit that reverses the order of qubits, i.e.,
    performs a SWAP such that [q1, q2, ..., qn] -> [qn, ... q2, q1].
    
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """
    for i in range( int(np.floor(n_qubits/2)) ):
        qml.SWAP( wires = [i, n_qubits-1-i])
    pass

def qft_rotations(n_qubits):
    """A circuit performs the QFT rotations on the specified qubits.
    
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """
    for i in range(n_qubits):
        qml.Hadamard(wires = i)
        for k in np.arange(2, n_qubits+1-i):
            # print("R %i, control qubit %i, acted qubit %i" % (k, k-1+i, i) )
            qml.ControlledPhaseShift(2*np.pi/2**k, wires = [int(k-1+i), i])
            
    pass

@qml.qnode(dev) 
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))
    qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qml.state()

@qml.qnode(dev) 
def circuit_qft(basis_id, n_qubits):
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))
    qml.QFT(wires=range(4))
    return qml.state()

print(qft_node(1, 4))
print(circuit_qft(1, 4))
