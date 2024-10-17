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
def circuit(alpha, theta):
    qml.RY(theta, wires = 0)
    qml.RY(theta, wires = 1)
    qml.Toffoli((0,1,2))
    qml.RY(70/9*theta, wires = 0)
    qml.RY(alpha*theta, wires = 1)
    return qml.probs(wires = [0,1,2])

dim_Alpha = 1000
dim_Theta = 1000
alpha = np.linspace(1, 4, dim_Alpha)
theta = np.linspace(0, 10, dim_Theta)
maxs = np.zeros(8)
max_record = np.zeros(dim_Alpha)
results = np.zeros([dim_Alpha, dim_Theta, 8])

limit = 0.9
y = np.zeros([dim_Theta, 8])

for i in range(len(alpha)):
    for j in range(len(theta)):
        results[i, j, :] = circuit(alpha[i], theta[j])
    maxs = [max(results[i, :, l]) for l in range(8)]
    max_record[i] = np.average(maxs)
    if max_record[i] > limit:
       print("Alpha fulfilling limit:")
       print(alpha[i])
       
       for k in range(8):
           y[:,k] = results[i, :, k]
           plt.plot(y[:,k])
       break

print("Average heigth:")
print(np.max(max_record))
# maxs = [ np.max(results[:, :, i]) for i in range(8)]
    
# print(maxs)
# circuit = [for i in theta]