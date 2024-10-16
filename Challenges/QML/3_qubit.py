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

dim_Alpha = 200
dim_Theta = 200
alpha = np.linspace(0, 10, dim_Alpha)
theta = np.linspace(0, 10, dim_Theta)
results = np.zeros([dim_Alpha, dim_Theta, 8])

limit = 0.9
y = np.zeros([dim_Theta, 8])

for i in range(len(alpha)):
    for j in range(len(theta)):
        @qml.qnode(dev)
        def circuit(alpha, theta):
            qml.RY(theta, wires = 0)
            qml.RY(theta, wires = 1)
            qml.Toffoli((0,1,2))
            qml.RY(70/9*theta, wires = 0)
            qml.RY(alpha*theta, wires = 1)
            return qml.probs(wires = [0,1,2])
        
        results[i, j, :] = circuit(alpha[i], theta[j])

    if (max(results[i, :, 0]) > limit) & (max(results[i, :, 1]) > limit) & (max(results[i, :, 2]) > limit) & (max(results[i, :, 3]) > limit) & (max(results[i, :, 4]) > limit) & (max(results[i, :, 5]) > limit) & (max(results[i, :, 6]) > limit) & (max(results[i, :, 7]) > limit):
       print(alpha[i])
       
       for k in range(8):
           y[:,k] = results[i, :, k]
           plt.plot(y[:,k])
       break
    

# circuit = [for i in theta]