#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:57:30 2024

@author: adria
"""

import numpy as np

H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
T = np.array([[1, 0], [0, np.exp(1j*np.pi/4)]])
HT = np.matmul(H,T)
HTH = np.matmul(HT,H)
print( HTH )