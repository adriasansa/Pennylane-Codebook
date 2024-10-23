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
def circuit(theta):
    for i in range(3):
        qml.Hadamard(i)
        qml.PhaseShift((4*theta)/2**i, wires = i)

    qml.adjoint(qml.QFT)(wires=[0,1,2])
    return qml.probs(wires = [0,1,2])

dim_Theta = 100
theta = np.linspace(0, 10, dim_Theta)

#%%
label = ["000","001","010","011","100","101","100","111"]
plt.figure()
for i in range(8):
    y = [circuit(theta[j])[i] for j in range(dim_Theta)] 
    plt.plot(theta, y,label = label[i])
plt.legend()