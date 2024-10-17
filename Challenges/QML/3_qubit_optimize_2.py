#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:05:49 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np
import matplotlib.pyplot as plt

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

def cost_function(alpha, beta):
    for i in range(dim_Theta):
        probs[i,:] = circuit(alpha, beta, theta[i])
    maxs = [max(probs[:, l]) for l in range(8)]
    max_record = np.average(maxs)
    return 1 - max_record


dim_Alpha = 100
dim_Beta = 100
alpha = np.linspace(0, 20, dim_Alpha)
beta = np.linspace(0, 20, dim_Beta)
y = np.zeros([dim_Alpha, dim_Beta])
limit = 0.01
for i in range(dim_Alpha):
    for j in range(dim_Beta):
        y[i, j] = cost_function(alpha[i], beta[j])
        if y[i,j] < limit:
            print(alpha[i])
            print(beta[j])
            break
    print("Completed...")
    print((i+1)/dim_Alpha)
            

# plt.plot(y)
print(np.min(y))
