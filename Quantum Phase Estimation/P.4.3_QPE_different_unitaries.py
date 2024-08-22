#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:09:39 2024

@author: adria
"""
import numpy as np
import pennylane as qml

dev = qml.device("default.qubit", wires=6)
estimation_wires = [0, 1, 2, 3]
target_wires = [4, 5]

def prepare_eigenvector_superposition(alpha, beta, gamma, delta):
    # Normalize alpha, beta, gamma, and delta
    norm_squared = np.abs(alpha) ** 2 + np.abs(beta) ** 2 + np.abs(gamma) ** 2 + np.abs(delta) ** 2 
    norm = np.sqrt(norm_squared)
    state = np.array([alpha/norm, beta/norm, gamma/norm, delta/norm])
    
    # Prepare the state
    qml.MottonenStatePreparation(state, wires=target_wires)


@qml.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.

    Returns:
        probs (array[float]): Probabilities on the estimation wires.
    """
    
    # MODIFY ALPHA, BETA, GAMMA, DELTA TO PREPARE EIGENVECTOR 
    #prepare_eigenvector_superposition(0, 0, 0, 1)
    #prepare_eigenvector_superposition(1, 0, 0, 0)
     #prepare_eigenvector_superposition(0, 1, 0, 0)
    prepare_eigenvector_superposition(1, 1, 1, 1)
    # OR UNCOMMENT LINES ABOVE TO PREPARE THE STATE OF YOUR CHOICE
    
    qml.QuantumPhaseEstimation(
        unitary,
        target_wires=target_wires,
        estimation_wires=estimation_wires,
    )
    return qml.probs(wires=estimation_wires)


# UNCOMMENT THE LINE CORRESPONDING TO THE MATRIX YOU'D LIKE 
# TO ESTIMATE PHASES OF
#U = qml.CZ.compute_matrix()
#U = qml.CRZ.compute_matrix(0.4)
U = qml.CRX.compute_matrix(1/3)
# U = qml.CRot.compute_matrix(0.9, 0.7, 0.4)

probs = qpe(U)

print(probs)

mystery_phase = 1/2+1/4+1/8+1/16 # MODIFY THIS
