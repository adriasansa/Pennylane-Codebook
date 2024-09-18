#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:58:03 2024

@author: adria
"""

import json
import pennylane as qml
import pennylane.numpy as np
def U_psi(theta):
    """
    Quantum function that generates |psi>, Zenda's state wants to send to Reece.

    Args:
        theta (float): Parameter that generates the state.

    """
    qml.Hadamard(wires = 0)
    qml.CRX(theta, wires = [0,1])
    qml.CRZ(theta, wires = [0,1])

def is_unsafe(alpha, beta, epsilon):
    """
    Boolean function that we will use to know if a set of parameters is unsafe.

    Args:
        alpha (float): parameter used to encode the state.
        beta (float): parameter used to encode the state.
        epsilon (float): unsafe-tolerance.

    Returns:
        (bool): 'True' if alpha and beta are epsilon-unsafe coefficients. 'False' in the other case.

    """
    dev = qml.device("default.qubit", wires=2)
    
    dev2 = qml.device("default.qubit", wires=2)

    def encoding_Operator(alpha, beta):
            qml.RZ(alpha, 0)
            qml.RX(beta, 0)

            qml.RZ(alpha, 1)
            qml.RX(beta, 1)  
            return
        
    @qml.qnode(dev)
    def psi_Density_Matrix(theta):
        U_psi(theta)
        return qml.density_matrix(wires = [0, 1])
    
    @qml.qnode(dev2)
    def circuit(theta, empty):
        
        U_psi(theta) #Eventually have to check out different thetas!!!

        density_Matrix = qml.Hermitian( psi_Density_Matrix(theta), wires = [0,1])
        
        encoding_Operator(alpha, beta)
        
        return qml.expval( -density_Matrix )
    
    # Rotosolve optimizer
    opt = qml.optimize.RotosolveOptimizer()
    num_steps = 4
    
    init_param = (
        np.array(0.0, requires_grad=True),
        np.array(0.5, requires_grad=False),
    )

    nums_frequency = {
        "theta": {(): 3}, #If 1 then analytic formula is used!
        "empty": {(): 1},
    }
    param = init_param

    for step in range(num_steps):
        param, cost = opt.step_and_cost(
            circuit,
            *param,
            nums_frequency=nums_frequency,
            # full_output=True,
            # rot_weights=rot_weights,
            # crot_weights=crot_weights,
            )
    # print(f"Cost before step: {cost}")
    # print(f"Minimization substeps: {np.round(sub_cost, 6)}")
    # cost_rotosolve.extend(sub_cost)
    
    # print(cost)
    F = -cost

    print(F)
    
    return F >= 1 - epsilon

# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    output = is_unsafe(*ins)
    return str(output)

def check(solution_output: str, expected_output: str) -> None:
    
    def bool_to_int(string):
        if string == "True":
            return 1
        return 0

    solution_output = bool_to_int(solution_output)
    expected_output = bool_to_int(expected_output)
    assert solution_output == expected_output, "The solution is not correct."

# These are the public test cases
test_cases = [
    ('[0.1, 0.2, 0.3]', 'True'),
    ('[1.1, 1.2, 0.3]', 'False'),
    ('[1.1, 1.2, 0.4]', 'True'),
    ('[0.5, 1.9, 0.7]', 'True')
]
# This will run the public test cases locally
for i, (input_, expected_output) in enumerate(test_cases):
    print(f"Running test case {i} with input '{input_}'...")

    try:
        output = run(input_)

    except Exception as exc:
        print(f"Runtime Error. {exc}")

    else:
        if message := check(output, expected_output):
            print(f"Wrong Answer. Have: '{output}'. Want: '{expected_output}'.")

        else:
            print("Correct!")