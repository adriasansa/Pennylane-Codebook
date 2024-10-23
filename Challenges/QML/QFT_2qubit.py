#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:05:49 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np
import matplotlib.pyplot as plt

num_wires = 2
dev = qml.device("default.qubit", wires=num_wires)
@qml.qnode(dev)
def circuit(theta):
    for i in range(num_wires):
        qml.Hadamard(i)
        qml.PhaseShift(theta/2**i, wires = i)

    qml.adjoint(qml.QFT)(wires=range(num_wires))
    return qml.probs(wires = range(num_wires))

dim_Theta = 100
theta = np.linspace(0, 10, dim_Theta)

#%%
label = ["00","01","10","11"]
plt.figure()
for i in range(2**num_wires):
    y = [circuit(theta[j])[i] for j in range(dim_Theta)] 
    plt.plot(theta, y,label = label[i])
plt.legend()