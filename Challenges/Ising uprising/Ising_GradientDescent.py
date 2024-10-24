#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:06:54 2024

@author: adria
"""

import json
import pennylane as qml
import pennylane.numpy as np
def create_Hamiltonian(h):
    """
    Function in charge of generating the Hamiltonian of the statement.

    Args:
        h (float): magnetic field strength

    Returns:
        (qml.Hamiltonian): Hamiltonian of the statement associated to h
    """
    obs_Z = qml.Z(0)@qml.Z(1)+ qml.Z(1)@qml.Z(2)+ qml.Z(2)@qml.Z(3)+ qml.Z(3)@qml.Z(0) 
    obs_X = qml.X(0)+qml.X(1)+ qml.X(2)+qml.X(3)
    obs = [obs_Z, obs_X]
    coeffs = [-1, -h]
    return qml.Hamiltonian(coeffs, obs)

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def model(params, H):
    """
    To implement VQE you need an ansatz for the candidate ground state!
    Define here the VQE ansatz in terms of some parameters (params) that
    create the candidate ground state. These parameters will
    be optimized later.

    Args:
        params (numpy.array): parameters to be used in the variational circuit
        H (qml.Hamiltonian): Hamiltonian used to calculate the expected value

    Returns:
        (float): Expected value with respect to the Hamiltonian H
    """
    for i in range(4):
        qml.RX(params[i, 0], wires = i)
        qml.RZ(params[i, 1], wires = i)
    
    return qml.expval(H)

def train(h):
    """
    In this function you must design a subroutine that returns the
    parameters that best approximate the ground state.

    Args:
        h (float): magnetic field strength

    Returns:
        (numpy.array): parameters that best approximate the ground state.
    """
    params_initial = np.array([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], requires_grad=True)
    
    def quant_fun(params):
        return model(params, create_Hamiltonian(h))
    
    theta = params_initial # Initial guess parameters
    angle = [theta] # Store the values of the circuit parameter
    cost = [quant_fun(theta)] # Store the values of the cost function

    opt = qml.GradientDescentOptimizer() # Our optimizer!
    max_iterations = 100 # Maximum number of calls to the optimizer 
    conv_tol = 1e-06 # Convergence threshold to stop our optimization procedure

    for n in range(max_iterations):
        theta, prev_cost = opt.step_and_cost(quant_fun, theta)
        cost.append(quant_fun(theta))
        angle.append(theta)

        conv = np.abs(cost[-1] - prev_cost)
        if n % 10 == 0:
            print(f"Step = {n},  Cost function = {cost[-1]:.8f} ")
        if conv <= conv_tol:
            break
    
    print("\n" f"Final value of the cost function = {cost[-1]:.8f} ")
    print("\n" f"Optimal value of the first circuit parameter =    "  + str(angle[-1][:][:]))
        
    return angle[-1][:][:]


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    params = train(ins)
    return str(model(params, create_Hamiltonian(ins)))


def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert np.allclose(
        solution_output, expected_output, rtol=1e-1
    ), "The expected value is not correct."

# These are the public test cases
test_cases = [
    ('1.0', '-5.226251859505506'),
    ('2.3', '-9.66382463698038')
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