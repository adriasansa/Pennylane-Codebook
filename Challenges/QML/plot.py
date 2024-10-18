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
# a = np.array([np.pi])
a = np.linspace(0,19.9, dim_a)
y = np.zeros(dim_a)
limit = 0.99

def plot_(alpha):
    y_0 = [np.cos(j/2)*np.cos(alpha*j/2) for j in x]
    y_1 = [np.cos(j/2)*np.sin(alpha*j/2) for j in x]
    y_2 = [np.sin(j/2)*np.sin(alpha*j/2) for j in x]
    y_3 = [np.sin(j/2)*np.cos(alpha*j/2) for j in x]
    
    plt.plot(y_0, label = "00")
    plt.plot(y_1, label = "10")
    plt.plot(y_2, label = "01")
    plt.plot(y_3, label = "11")
    plt.legend()

for i in range(len(a)):
    y_0 = [np.cos(j/2)*np.cos(a[i]*j/2) for j in x]
    y_1 = [np.cos(j/2)*np.sin(a[i]*j/2) for j in x]
    y_2 = [np.sin(j/2)*np.sin(a[i]*j/2) for j in x]
    y_3 = [np.sin(j/2)*np.cos(a[i]*j/2) for j in x]
    
    # plt.plot(y_0)
    # plt.plot(y_1)
    # plt.plot(y_2)
    # plt.plot(y_3)
    
    max_0 = float(np.max(y_0))
    max_1 = float(np.max(y_1))
    max_2 = float(np.max(y_2))
    max_3 = float(np.max(y_3))
    y[i] = np.average([max_0, max_1, max_2, max_3])
    if (max_0 >limit) & (max_1 >limit) & (max_2 >limit) & (max_3 >limit):
        # print(max_0)
        # print(max_1)
        # print(max_2)
        # print(max_3)
        
        print("a=")
        print(a[i])    
        # plt.plot(y_0)
        # plt.plot(y_1)
        # plt.plot(y_2)
        # plt.plot(y_3)
        
        # break
    
plt.plot(x, y)