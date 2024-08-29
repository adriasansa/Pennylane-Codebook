#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:49:44 2024

@author: adria
"""

import numpy as np
import pennylane as qml

dev = qml.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qml.PauliX(wires=target_wires)


@qml.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.
        
    Returns:
        array[float]: Probabilities on the estimation wires.
    """
    
    prepare_eigenvector()
    qml.QuantumPhaseEstimation(unitary, target_wires=target_wires, estimation_wires=estimation_wires)
    return qml.probs(wires = estimation_wires)

def estimate_phase(probs):
    """Estimate the value of a phase given measurement outcome probabilities
    of the QPE routine.
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
    
    Returns:
        float: the estimated phase   
    """
    
    probs_round = [np.round(probs[i]) for i in range(len(probs))]
    probs_bin = '{0:03b}'.format(probs_round.index(1))
    phase = sum([ int(probs_bin[i])/2**(i+1) for i in np.arange(len(probs_bin))])
    return float(phase)

U = qml.T.compute_matrix()

probs = qpe(U)


estimated_phase = estimate_phase(probs)
print(estimated_phase)

