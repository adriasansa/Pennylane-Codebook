#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:05:49 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, differential_evolution

dev = qml.device("default.qubit", wires=3)
@qml.qnode(dev)
def circuit(alpha, beta, theta):
    qml.RY(theta, wires = 0)
    qml.RY(theta, wires = 1)
    qml.Toffoli((0,1,2))
    qml.RY(alpha*theta, wires = 0)
    qml.RY(beta*theta, wires = 1)
    return qml.probs(wires = [0,1,2])

dim_Theta = 100
theta = np.linspace(0, 10, dim_Theta)
probs = np.zeros([len(theta), 8])
maxs = np.zeros(8)
max_record = 0

def cost_function(params):
    alpha, beta = params
    for i in range(dim_Theta):
        probs[i,:] = circuit(alpha, beta, theta[i])
    maxs = [max(probs[:, l]) for l in range(8)]
    max_record = np.average(maxs)
    return 1 - max_record

bounds = [(0, 10), (0, 10)]
res = differential_evolution(cost_function, bounds)
print(res.fun)
print(res.x) # E.g. [7.86614467 6.19630591]

alpha_optimal = res.x[0]
beta_optimal = res.x[1]
#%%
dim_Theta = 1000
theta = np.linspace(0, 10, dim_Theta)
for i in range(8):
    y = [circuit(alpha_optimal, beta_optimal, theta[j])[i] for j in range(dim_Theta)] 
    plt.plot(theta, y)