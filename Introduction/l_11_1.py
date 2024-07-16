#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:11:49 2024

@author: adria
"""

import numpy as np
import pennylane as qml

num_wires = 3
dev = qml.device("default.qubit", wires=num_wires)


@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.

    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        np.array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    binary = np.binary_repr(basis_id)
    binary = binary.zfill(num_wires)
    

    # CREATE THE BASIS STATE
    
    for i in np.arange(num_wires):
        if int(binary[i]) == 1:
            qml.PauliX(wires = int(i))

    return qml.state()


basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")