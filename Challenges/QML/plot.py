#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:21:48 2024

@author: adria
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,10, 100)
a = np.linspace(0,2, 100)

limit = 0.8

for i in a:
    y_0 = [np.cos(i/2)*np.cos(a*i/2) for i in x]
    y_1 = [np.cos(i/2)*np.sin(a*i/2) for i in x]
    y_2 = [np.sin(i/2)*np.sin(a*i/2) for i in x]
    y_3 = [np.sin(i/2)*np.cos(a*i/2) for i in x]
    
    max_0 = float(np.max(y_0))
    max_1 = float(np.max(y_1))
    max_2 = float(np.max(y_2))
    max_3 = float(np.max(y_3))
    if (max_0 >limit) & (max_1 >limit) & (max_2 >limit) & (max_3 >limit):
        print(max_0)
        print(max_1)
        print(max_2)
        print(max_3)
        
        
        print(i)    
        plt.plot(y_0)
        plt.plot(y_1)
        plt.plot(y_2)
        plt.plot(y_3)
        
        break