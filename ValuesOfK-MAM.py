#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 18:53:48 2025

@author: jackiefu
"""

import matplotlib.pyplot as plt

# Constants
G = 613.5
b = 0.8052
k = 0.2041
Y_eq = G / (1 - b)  # Theoretical equilibrium

# Initialize Y with two initial values
Y = [0, 10]  # Y[0] = 0, Y[1] = 10 (arbitrary to start dynamics)

# Simulate the model for 30 time periods
for t in range(2, 30):
    Yt = G + (b + b * k) * Y[t - 1] - b * k * Y[t - 2]
    Y.append(Yt)

# Time axis
time = list(range(30))

# Plot from t = 1 onward
plt.figure(figsize=(8, 5))
plt.plot(time[1:], Y[1:], color='black', label=f'b={b}, k={k}')
plt.axhline(y=Y_eq, color='black', linestyle='--', label=f'Equilibrium Y* = {Y_eq:.2f}')
plt.xlabel('t')
plt.ylabel('Y')
plt.grid(False)
plt.show()
