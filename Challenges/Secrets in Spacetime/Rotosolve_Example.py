#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:41:37 2024

@author: adria
"""

import pennylane as qml
import pennylane.numpy as np


opt = qml.optimize.RotosolveOptimizer()
num_steps = 3

dev = qml.device('default.qubit', wires=3, shots=None)

@qml.qnode(dev)
def function(theta, empty):
    qml.RX(theta, wires = 0)
    qml.RY(theta, wires = 1)
    qml.RZ(theta, wires = 2)
    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1) @ qml.PauliZ(2))

init_param = (
    np.array(0.0, requires_grad=True),
    np.array(0.5, requires_grad=False),
)

nums_frequency = {
    "theta": {(): 3}, #If 1 then analytic formula is used!
    "empty": {(): 3},
}

param = init_param
cost_rotosolve = []
for step in range(num_steps):
    param, cost = opt.step_and_cost(
        function,
        *param,
        nums_frequency=nums_frequency,
        # full_output=True,
    )
    print(f"Cost before step: {cost}")