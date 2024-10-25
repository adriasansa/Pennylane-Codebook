#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:38:48 2024

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

    qml.ArbitraryStatePreparation(params, wires=[0, 1, 2, 3])
    
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

    H = create_Hamiltonian(h)
    
    opt_kwargs = {"num_steps": 5}
    opt = qml.optimize.RotosolveOptimizer(substep_optimizer="brute", substep_kwargs=opt_kwargs)
    num_steps = 4
    
    init_angles = np.zeros(30, requires_grad=True)
    # import random
    # for i in range(4):
    #     for j in range(2):
    #         init_angles[i][j] = random.random()*np.pi
    
    init_param = (
        np.array(init_angles, requires_grad=True),
        H,
    )

    nums_frequency = {
        "params": {(0,): 1, (1,): 1, (2,): 1, (3,): 1, (4,): 1, (5,): 1, (6,): 1, (7,): 1, (8,): 1, (9,): 1, (10,): 1,
                   (10,): 1, (11,): 1, (12,): 1, (13,): 1, (14,): 1, (15,): 1, (16,): 1, (17,): 1, (18,): 1, (19,): 1,
                   (20,): 1, (21,): 1, (22,): 1, (23,): 1, (24,): 1, (25,): 1, (26,): 1, (27,): 1, (28,): 1, (29,): 1,
                   },
    }

    param = init_param
    cost_rotosolve = []
    for step in range(num_steps):
        param, cost, sub_cost = opt.step_and_cost(
            model,
            *param,
            nums_frequency=nums_frequency,
            full_output=True,
        )
        # print(f"Cost before step: {cost}")
        # print(f"Minimization substeps: {np.round(sub_cost, 6)}")
        cost_rotosolve.extend(sub_cost)
        
    print(cost)
    # print(param[0][:][:])
    return param[0][:][:]


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