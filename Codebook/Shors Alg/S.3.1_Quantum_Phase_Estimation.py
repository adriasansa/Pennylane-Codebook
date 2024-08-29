#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:38:29 2024

@author: adria
"""
import numpy as np
import pennylane as qml

def U():
    qml.SWAP(wires=[2, 3])
    qml.SWAP(wires=[1, 2])
    qml.SWAP(wires=[0, 1])
    for i in range(4):
        qml.PauliX(wires=i)


matrix = qml.matrix(U, wire_order=range(4))()

n_target_wires = 4
target_wires = range(n_target_wires)
n_estimation_wires = 3
estimation_wires = range(4, 4 + n_estimation_wires)


dev = qml.device("default.qubit", shots=1, wires=n_target_wires + n_estimation_wires)


@qml.qnode(dev)
def circuit(matrix):
    """Return a sample after taking a shot at the estimation wires.

    Args:
        matrix (array[complex]): matrix representation of U.

    Returns:
        array[float]: a sample after taking a shot at the estimation wires.
    """

    # CREATE THE INITIAL STATE |0001> ON TARGET WIRES
    qml.PauliX(wires = target_wires[-1])
    # USE THE SUBROUTINE QUANTUM PHASE ESTIMATION
    qml.QuantumPhaseEstimation(matrix, target_wires = target_wires, estimation_wires = estimation_wires)
    return qml.sample(wires=estimation_wires)


def get_phase(matrix):
    binary = "".join([str(b) for b in circuit(matrix)])
    return int(binary, 2) / 2**n_estimation_wires


for i in range(5):
    print(circuit(matrix))
    print(f"shot {i+1}, phase:", get_phase(matrix))
