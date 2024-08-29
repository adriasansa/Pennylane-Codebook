#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:31:46 2024

@author: adria
"""

from sympy import Symbol, sin, cos, I, exp, ImmutableMatrix
from sympy.physics.quantum import qapply
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.gate import UGate

theta = Symbol('theta')
alpha = Symbol('alpha')
beta = Symbol('beta')

Rz_theta_mat = ImmutableMatrix([[exp(-I*theta/2), 0],
                        [0, exp(I*theta/2)]])
Rx_theta_mat = ImmutableMatrix([[cos(theta/2), -I*sin(theta/2)],
                        [-I*sin(theta/2) ,cos(theta/2)]])

Rz_alpha_mat = ImmutableMatrix([[exp(-I*alpha/2), 0],
                        [0, exp(I*alpha/2)]])

Rx_beta_mat = ImmutableMatrix([[cos(beta/2), -I*sin(beta/2)],
                        [-I*sin(beta/2) ,cos(beta/2)]])

Rz_theta = UGate((0,), Rz_theta_mat)
Rx_theta = UGate((0,), Rx_theta_mat)

Rz_alpha = UGate((0,), Rz_alpha_mat)
Rx_beta = UGate((0,), Rx_beta_mat)

print(qapply(Rz_alpha*Rx_beta*Rz_theta*Rx_theta*Qubit('0'))) # -sin(theta/2)**2*|00> + 2*sin(theta/2)*cos(theta/2)*|01> + cos(theta/2)**2*|00>