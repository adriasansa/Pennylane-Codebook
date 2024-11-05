#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:34:46 2024

@author: adria
"""

import json
import pennylane as qml
import pennylane.numpy as np
# Write any helper functions you need here

# import random
num_Loops = 5 # Loops of the QAOA alg
max_iterations = 100 # Maximum number of calls to the optimizer 

def cost_hamiltonian(edges):
    """
    This function build the QAOA cost Hamiltonian for a graph, encoded in its edges

    Args:
    - Edges (list(list(int))): A list of ordered pairs of integers, representing 
    the edges of the graph for which we need to solve the minimum vertex cover problem.

    Returns:
    - pennylane.Operator: The cost Hamiltonian associated with the graph.
    """
    # Put your code here #
    shape = np.shape(edges)
    
    obs_edges = 0
    for i in range(shape[0]):
        obs_edges += qml.Z(wires=edges[i][0])@qml.Z(wires=edges[i][1])+qml.Z(wires=edges[i][0])+qml.Z(wires=edges[i][1])
    
    obs_vertices = 0
    for i in range(np.max(edges)):
        obs_vertices += qml.Z(wires = i)
    
    obs = [obs_edges, obs_vertices]
    coeffs = [3/4, -1]
    return qml.Hamiltonian(coeffs, obs)
    

def mixer_hamiltonian(edges):
    """
    This function build the QAOA mixer Hamiltonian for a graph, encoded in its edges

    Args:
    - edges (list(list(int))): A list of ordered pairs of integers, representing 
    the edges of the graph for which we need to solve the minimum vertex cover problem.

    Returns:
    - pennylane.Operator: The mixer Hamiltonian associated with the graph.
    """

    # Put your code here #
    obs_vertices = 0
    for i in range(np.max(edges)):
        obs_vertices += qml.X(wires = i)
    
    obs = [obs_vertices]
    coeffs = [1]
    return qml.Hamiltonian(coeffs, obs)

def qaoa_circuit(params, edges):
    """
    This quantum function (i.e. a list of gates describing a circuit) implements the QAOA algorithm
    You should only include the list of gates, and not return anything

    Args:
    - params (np.array): A list encoding the QAOA parameters. You are free to choose any array shape you find 
    convenient.
    - edges (list(list(int))): A list of ordered pairs of integers, representing 
    the edges of the graph for which we need to solve the minimum vertex cover problem.

    Returns:
    - This function does not return anything. Do not write any return statements.
    
    """
    # Put your code here
    
    # Initialization
    for i in range(np.max(edges)):
        qml.Hadamard(wires = i)
        
    # Loops
    for i in range(num_Loops):
        qml.exp(cost_hamiltonian(edges), -1j*params[i][0], num_steps = 2) #2*np.pi*
        qml.exp(mixer_hamiltonian(edges), -1j*params[i][1], num_steps = 2) #np.pi*
    
# This function runs the QAOA circuit and returns the expectation value of the cost Hamiltonian

dev = qml.device("default.qubit")

@qml.qnode(dev)
def qaoa_expval(params, edges):
    qaoa_circuit(params, edges)
    return qml.expval(cost_hamiltonian(edges))

def optimize(edges):
    """
    This function returns the parameters that minimize the expectation value of
    the cost Hamiltonian after applying QAOA

    Args:
    - edges (list(list(int))): A list of ordered pairs of integers, representing 
    the edges of the graph for which we need to solve the minimum vertex cover problem.

    
    """

    # Your cost function should be the expectation value of the cost Hamiltonian
    # You may use the qaoa_expval QNode defined above
    
    # Write your optimization routine here
    
    params_initial = np.ones([num_Loops,2], requires_grad=True)
    eta = 0.01
    # import random
    # for i in range(30):
    #     init_params[i] = random.random()*np.pi
    
    theta = [params_initial, edges] # Initial guess parameters
    angle = [theta] # Store the values of the circuit parameter
    cost = [qaoa_expval(*theta)] # Store the values of the cost function
    
    opt = qml.QNGOptimizer(eta)

    max_iterations = 100 # Maximum number of calls to the optimizer 
    conv_tol = 1e-04 # Convergence threshold to stop our optimization procedure
    
    for n in range(max_iterations):
        theta, prev_cost = opt.step_and_cost(qaoa_expval, *theta)
        cost.append(qaoa_expval(*theta))
        angle.append(theta)

        conv = np.abs(cost[-1] - prev_cost)
        if n % 10 == 0:
            print(f"Step = {n},  Cost function = {cost[-1]:.8f} ")
        if conv <= conv_tol:
            break
    
    print("\n" f"Final value of the cost function = {cost[-1]:.8f} ")
    print("\n" f"Optimal value of the first circuit parameter =    "  + str(angle[-1][0][:]))
    # print(angle[-1][0][:][:])
    
    return angle[-1][0][:]
    
# These are auxiliary functions that will help us grade your solution. Feel free to check them out!

@qml.qnode(dev)
def qaoa_probs(params, edges):
  qaoa_circuit(params, edges)
  return qml.probs()

def approximation_ratio(params, edges):

    true_min = np.min(qml.eigvals(cost_hamiltonian(edges)))
    print("True min:")
    print(true_min)
    approx_ratio = qaoa_expval(params, edges)/true_min

    return approx_ratio

# These functions are responsible for testing the solution.

def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    params = optimize(ins)
    output= approximation_ratio(params,ins).numpy()

    ground_energy = np.min(qml.eigvals(cost_hamiltonian(ins)))

    index = np.argmax(qaoa_probs(params, ins))
    vector = np.zeros(len(qml.matrix(cost_hamiltonian(ins))))
    vector[index] = 1

    calculate_energy = np.real_if_close(np.dot(np.dot(qml.matrix(cost_hamiltonian(ins)), vector), vector))
    verify = np.isclose(calculate_energy, ground_energy)

    if verify:
      return str(output)
    
    return "QAOA failed to find right answer"

def check(solution_output: str, expected_output: str) -> None:

    assert not solution_output == "QAOA failed to find right answer", "QAOA failed to find the ground eigenstate."
        
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert solution_output >= expected_output-0.01, "Minimum approximation ratio not reached"

# These are the public test cases
test_cases = [
    ('[[0, 1], [1, 2], [0, 2], [2, 3]]', '0.55'),
    ('[[0, 1], [1, 2], [2, 3], [3, 0]]', '0.92'),
    ('[[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4]]', '0.55')
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