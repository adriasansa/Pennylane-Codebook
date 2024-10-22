#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:21:48 2024

@author: adria
"""

import numpy as np
import matplotlib.pyplot as plt

dim_a = 1000

x = np.linspace(0,10, dim_a)
y = np.zeros(dim_a)


def plot():
    y_0 = [(np.cos(j)*np.cos(j/2) )**2 for j in x]
    y_1 = [(np.cos((j-np.pi/2))*np.cos((j-np.pi/2)/2) )**2 for j in x]
    y_2 = [(np.cos((j-np.pi))*np.cos((j-np.pi)/2) )**2 for j in x]
    y_3 = [(np.cos((j-3*np.pi/2))*np.cos((j-3*np.pi/2)/2) )**2 for j in x]
    
    plt.plot(y_0, label = "00")
    plt.plot(y_1, label = "10")
    plt.plot(y_2, label = "01")
    plt.plot(y_3, label = "11")
    plt.legend()

plot()