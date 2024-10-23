#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:05:49 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np
import matplotlib.pyplot as plt

unitary = np.zeros([8,8])


dev = qml.device("default.qubit", wires=3)
@qml.qnode(dev)
def circuit(theta):
    qml.Hadamard(0)
    qml.Hadamard(1)
    qml.Hadamard(2)
    
    for i in range(8):
        for j in range(8):
            unitary[i,j] = np.cos((theta-np.pi/4*i)/2)*np.cos(theta-np.pi/4*i)*np.cos((theta-np.pi/4*i)*2)
    
    qml.QubitUnitary(unitary, wires = [0,1,2])
    return qml.probs(wires = [0,1,2])

dim_Theta = 100
theta = np.linspace(0, 10, dim_Theta)

for i in range(8):
    y = [circuit(theta[j])[i] for j in range(dim_Theta)] 
    plt.plot(theta, y)