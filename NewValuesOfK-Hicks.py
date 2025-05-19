#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 12:27:42 2025

@author: jackiefu
"""

import matplotlib.pyplot as plt

# Constants
g = 0.0254
A = 205.8565
B = 189.7813
T = 30  # number of time periods

# Particular solution: Y_t = A*(1+g)^t
AQ = 2391.2248

# Initialize Y with two starting values: Y[0] and Y[1]
Y = [0]  # arbitrary initial conditions

# Simulate backward-looking form: Y_t = (b+k)*Y_{t-1} - k*Y_{t-2} + a*(1+g)^t
for t in range(1, T):
    Yt = A * (0.7652)**t - B * (0.1954)**t + 2391.2248 * (1 + g)**t
    Y.append(Yt)

# Time axis starting from t = 2
time = list(range(1, T))

# Trim Y and equilibrium path to start at t = 2
Y_plot = Y[1:]
Y_eq_plot = [AQ * (1 + g)**t for t in time]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(time, Y_plot, color='black')
plt.plot(time, Y_eq_plot, '--', color='black')
plt.xlabel('t')
plt.ylabel('Y')
plt.show()

# Error calculation starting from t = 2
t = 2
while t < min(len(Y), 30):  # Ensure we don't go out of bounds
    Y_real = Y[t]
    Y_eq = A * (1 + g)**t
    error = Y_real - Y_eq
    print(f"t = {t}, Error = {error:.6f}")
    t += 1
