#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:21:48 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

dev = qml.device("default.qubit", wires=2)
@qml.qnode(dev)
def circuit(alpha, theta):
    qml.RY(theta, wires = 0)
    qml.CNOT((0,1))
    qml.RY(alpha*theta, wires = 0)
    return qml.probs(wires = [0,1])

dim_Theta = 200
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


res = minimize(cost_function, (5) ,method='Nelder-Mead', tol=1e-3)
print(res.fun)
print(res.x)

for i in range(4):
    y = [circuit(res.x[0],  theta[j])[i] for j in range(dim_Theta)] 
    plt.plot(theta, y)