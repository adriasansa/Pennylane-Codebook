#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:05:49 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np

dev = qml.device("default.qubit", wires=3)

alpha = np.linspace(0, 10, 100)
theta = np.linspace(0, 10, 100)
results = np.zeros([100, 100])
limit = 0.5

for i in alpha:
    for j in theta:
        @qml.qnode(dev)
        def circuit(alpha, theta):
            qml.RY(theta, wires = 0)
            qml.RY(theta, wires = 1)
            qml.Toffoli((0,1,2))
            qml.RY(70/9*theta, wires = 0)
            qml.RY(theta, wires = 1)
            return qml.probs(wires = [0,1,2])
        
        results[i, j] = circuit(i, j)

# circuit = [for i in theta]