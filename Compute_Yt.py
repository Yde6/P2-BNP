import numpy as np

# Parameters
lambda1 = 0.75105
lambda2 = 0.21845
Y1_0 = 2407.3
Y2_0 = 2572.4
G = 613.5

def compute_Yt(t):
    # Precompute common terms
    lambda1_t = lambda1 ** t
    lambda2_t = lambda2 ** t
    lambda1_t1 = lambda1 ** (t + 1)
    lambda2_t1 = lambda2 ** (t + 1)
    denom = lambda2 - lambda1
    
    # Matrix A
    A11 = (lambda1_t * lambda2 - lambda1 * lambda2_t) / denom
    A12 = (lambda2_t - lambda1_t) / denom
    A21 = (lambda1_t1 * lambda2 - lambda1 * lambda2_t1) / denom
    A22 = (lambda2_t1 - lambda1_t1) / denom
    A = np.array([[A11, A12], [A21, A22]])
    
    # Matrix B
    B11 = A11 - 1
    B12 = A12
    B21 = A21
    B22 = A22 - 1
    B = np.array([[B11, B12], [B21, B22]])
    
    # Matrix C
    C = np.array([[-1, 1], [-lambda1 * lambda2, lambda1 + lambda2 - 1]])
    
    # Compute C inverse
    C_inv = np.linalg.inv(C)
    
    # Vector [0, G]
    G_vec = np.array([0, G])
    
    # Initial conditions vector
    Y0 = np.array([Y1_0, Y2_0])
    
    # Compute Y_t
    Y_t = A @ Y0 + B @ C_inv @ G_vec
    
    return Y_t

# Compute and display results for t = 0 to 5
t_values = range(6)
print("t | Y_1(t) | Year (Y_1) | Y_2(t) | Year (Y_2)")
print("-" * 50)
for t in t_values:
    Y_t = compute_Yt(t)
    year_Y1 = 2021 + t
    year_Y2 = 2022 + t
    print(f"{t} | {Y_t[0]:.2f} | {year_Y1} | {Y_t[1]:.2f} | {year_Y2}")

# Optionally, compute for specific years (2023-2027 using Y_2(t))
print("\nYear | Value")
print("-" * 20)
for t in range(1, 6):
    Y_t = compute_Yt(t)
    year = 2022 + t
    print(f"{year} | {Y_t[1]:.2f}")