#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:05:49 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=2)
@qml.qnode(dev)
def circuit(theta):
    qml.RX(theta, wires = 0)
    qml.CNOT((0,1))
    qml.RX(2*theta, wires = 0)
    qml.RY(np.pi, wires = 1)
    # qml.Hadamard(0)
    # qml.Hadamard(1)
    # unitary = 2*np.array([[np.cos(theta)*np.cos(theta/2),0,0,0],
    #            [0,np.sin(theta)*np.cos((theta-np.pi/2)/2),0,0],
    #            [0,0,-np.cos(theta)*np.sin(theta/2),0],
    #            [0,0,0,-np.sin(theta)*np.cos((theta+np.pi/2)/2)]])
    # qml.QubitUnitary(unitary, wires = [0,1], unitary_check=True)
    return qml.probs(wires = [0,1])

dim_Theta = 100
theta = np.linspace(0, 10, dim_Theta)

#%%
label = ["00","01","10","11"]
plt.figure()
for i in range(4):
    y = [circuit(theta[j])[i] for j in range(dim_Theta)] 
    plt.plot(theta, y,label = label[i])
plt.legend()