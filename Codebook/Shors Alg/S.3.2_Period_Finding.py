#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:58:38 2024

@author: adria
"""

# Only running in codebook, assumes we have get_phase :( , get_phase in turn assumes we know the eigenvector and prepare it in the estimation wires

import pennylane as qml
import fractions


def U():
    qml.SWAP(wires=[2, 3])
    qml.SWAP(wires=[1, 2])
    qml.SWAP(wires=[0, 1])
    for i in range(4):
        qml.PauliX(wires=i)


matrix = qml.matrix(U, wire_order=range(4))()

target_wires = range(4)
n_estimation_wires = 3
estimation_wires = range(4, 4 + n_estimation_wires)


def get_period(matrix):
    """Return the period of the state using the already-defined
    get_phase function.

    Args:
        matrix (array[complex]): matrix associated with the operator U

    Returns:
        int: Obtained period of the state.
    """

    shots = 10
    fraction = []
    denominator = 0
    for i in range(shots):
        shot = fractions.Fraction( get_phase(matrix)).limit_denominator(2 ** n_estimation_wires)
        
        if shot.denominator > denominator:
            denominator = shot.denominator
        
        fraction.append( shot )
    print(fraction)
    return denominator


print(get_period(matrix))

