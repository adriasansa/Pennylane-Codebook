#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:21:48 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=2)
@qml.qnode(dev)
def circuit(alpha, theta):
    qml.RY(theta, wires = 0)
    qml.CNOT((0,1))
    qml.RY(alpha*theta, wires = 0)
    return qml.probs(wires = [0,1])

dim_Theta = 100
theta = np.linspace(0, 10, dim_Theta)
probs = np.zeros([len(theta), 4])
maxs = np.zeros(4)
max_record = 0

def cost_function(alpha):
    for i in range(dim_Theta):
        probs[i,:] = circuit(alpha, theta[i])
    maxs = [max(probs[:, l]) for l in range(4)]
    max_record = np.average(maxs)
    return 1 - max_record


dim_Alpha = 100
alpha = np.linspace(0, 10, dim_Alpha)
y = np.zeros(dim_Alpha)
for i in range(dim_Alpha):
    y[i] = cost_function(alpha[i])

plt.plot(y)
print(min(y))