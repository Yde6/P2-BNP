#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  6 14:46:15 2025

@author: jackiefu
"""

import matplotlib.pyplot as plt
import numpy as np

# Define k range
k = np.linspace(0.01, 5, 500)  # start from 0.01 to avoid division by zero

# Define the curve
b1 = np.sqrt(4*k) - k

# Estimate the intersection point (P) numerically with b = 1
b2_val = 1
idx_p = np.argmin(np.abs(b1 - b2_val))
k_p = k[idx_p]
b_p = b1[idx_p]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(k, b1, label=r'$b = \sqrt{4k} - k$', color='black')
plt.axvline(x=1, color='black', linestyle='--', label=r'$k = 1$')  # vertical line at k=1

# Annotate curves and regions
plt.text(0.18, 0.9, 'A', fontsize=12, weight='bold')
plt.text(0.5, 0.25, 'B', fontsize=12, weight='bold')
plt.text(2, 0.3, 'C', fontsize=12, weight='bold')
plt.text(3.8, 0.7, 'D', fontsize=12, weight='bold')
plt.text(1.05, 1.05, r'$k = 1$', fontsize=12, weight='bold')
plt.text(4, 0.1, r'$b = \sqrt{4k} - k$', fontsize=12, weight='bold')

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
