#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 12:35:43 2025

@author: jackiefu
"""

import matplotlib.pyplot as plt
import numpy as np

# Define k range
k = np.linspace(0.01, 5, 500)  # start from 0.01 to avoid division by zero

# Define the curves
b1 = 4 * k / (1 + k)**2
b2 = 1 / k

# Estimate the intersection point (P) numerically
idx_p = np.argmin(np.abs(b1 - b2))
k_p = k[idx_p]
b_p = b1[idx_p]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(k, b1, label=r'$b = \frac{4k}{(1 + k)^2}$', color='black')
plt.plot(k, b2, label=r'$b = \frac{1}{k}$', color='black', linestyle='--')

# Annotate curves and regions
plt.text(0.2, 0.9, 'A', fontsize=12, weight='bold')
plt.text(1.1, 0.25, 'B', fontsize=12, weight='bold')
plt.text(2.7, 0.55, 'C', fontsize=12, weight='bold')
plt.text(3.5, 0.85, 'D', fontsize=12, weight='bold')
plt.text(4.65, 0.14, r'$b = \frac{1}{k}$', fontsize=12, weight='bold')
plt.text(4.45, 0.5, r'$b = \frac{4k}{(1 + k)^2}$', fontsize=12, weight='bold')

# Point P
plt.plot(k_p, b_p, 'ko')  # black dot

# Horizontal line at b = 1
plt.axhline(1.0, color='black', linestyle='-.', linewidth=1)

# Axis labels
plt.xlabel('k')
plt.ylabel('b')

plt.xlim(0, 5)
plt.ylim(0, 1.2)
plt.yticks([1.0])  # Show only 1.0 on the y-axis
plt.show()
