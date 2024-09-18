#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:03:43 2024

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
    
    @qml.qnode(dev)
    def circuit(theta):
        
        U_psi(theta) #Eventually have to check out different thetas!!!

        density_Matrix = qml.Hermitian( psi_Density_Matrix(theta), wires = [0,1])
        encoding_Operator(alpha, beta)
        
        return qml.expval( density_Matrix )
    
    
    # Define your Hamiltonian 
    theta = np.array(3.0, requires_grad=True) # Initial guess parameters -> It works for initial parameter = 0.0 but not for 3.0
    angle = [theta] # Store the values of the circuit parameter
    cost = [circuit(theta)] # Store the values of the cost function

    opt = qml.GradientDescentOptimizer(stepsize=0.5) # Our optimizer!
    max_iterations = 100 # Maximum number of calls to the optimizer 
    conv_tol = 1e-06 # Convergence threshold to stop our optimization procedure
    
    for n in range(max_iterations):
        theta, prev_cost = opt.step_and_cost(lambda params: -circuit(params), theta)
        cost.append(circuit(theta))
        angle.append(theta)
        conv = np.abs(np.abs(cost[-1]) - np.abs(prev_cost))
        if n % 10 == 0:
            # print(cost[-1])
            # print(f"Step = {n}, " + "Cost function = " + str(cost[-1]) )
            if conv <= conv_tol:
                break
    
    # print("\n" f"Final value of the cost function = {cost[-1]:.8f} ")
    import matplotlib.pyplot as plt
    plt.plot(cost)
    # plt.plot(angle)
    plt.show(block = True)
    F = cost[-1]

    print(F)
    return F > 1 - epsilon

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