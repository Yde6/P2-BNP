#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 12:27:42 2025

@author: jackiefu
"""

import matplotlib.pyplot as plt

# Constants
g = 0.02
b = 0.8
k = 1.1
a = 100
T = 30  # number of time periods

# Particular solution: Y_t = A*(1+g)^t
A = a*(1+g)**2 / ((1+g)**2 - (b + k)*(1 + g) + k)

# Initialize Y with two starting values: Y[0] and Y[1]
Y = [0, 10]  # arbitrary initial conditions

# Simulate backward-looking form: Y_t = (b+k)*Y_{t-1} - k*Y_{t-2} + a*(1+g)^t
for t in range(2, T):
    Yt = (b + k) * Y[t - 1] - k * Y[t - 2] + a * (1 + g)**t
    Y.append(Yt)

# Time axis starting from t = 1
time = list(range(1, T))

# Trim Y and equilibrium path to start at t = 1
Y_plot = Y[1:]
Y_eq_plot = [A * (1 + g)**t for t in time]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(time, Y_plot, label='Simulated Y', color='black')
plt.plot(time, Y_eq_plot, '--', label='Equilibrium path $Y_t^*$', color='black')
plt.xlabel('t')
plt.ylabel('Y')
plt.show()

t = 1
while t < min(len(Y), 30):  # Ensure we don't go out of bounds
    Y_real = Y[t]
    Y_eq = A * (1 + g)**t
    error = Y_real - Y_eq
    print(f"t = {t}, Error = {error:.6f}")
    t += 1