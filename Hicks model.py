import numpy as np
import matplotlib.pyplot as plt

# Global variables for easy modification
Y0 = 2407.3  # Initial condition Y_0^(1)
Y1 = 2572.4  # Initial condition Y_1^(1)
a = 491.11  # Parameter a
b = 0.815  # Parameter b
k = 0.1813  # Parameter k
g = 0.0254  # Parameter g
NUM_STEPS = 10  # Number of time stepss

def solve_difference_equation_iteratively():
    """
    Solve the difference equation iteratively ensuring Y_{t+1}^(1) = Y_t^(2).
    
    Returns:
    Y: Array of solutions [Y_t^(1), Y_t^(2)] for each time step
    """
    # Initialize the state vector Y
    Y = np.zeros((NUM_STEPS + 1, 2))
    Y[0, 0] = Y0  # Y_0^(1)
    Y[0, 1] = Y1  # Y_0^(2), setting Y_0^(2) = Y_1^(1) as per user input
    
    # Define the coefficient matrix A
    A = np.array([[0, 1],
                  [-k, (b + k)]])
    
    # Compute solution iteratively
    for t in range(NUM_STEPS):
        # Forcing term at time t
        forcing = np.array([0, a * (1 + g)**(t + 2)])
        # Compute Y_{t+1} = A * Y_t + forcing
        Y[t + 1, :] = A @ Y[t, :] + forcing
    
    return Y

# Run the solver, print results, and plot
if __name__ == "__main__":
    solution = solve_difference_equation_iteratively()
    
    # Print results
    print("Time step | Y_t^(1) | Y_t^(2)")
    print("-----------------------------")
    for t in range(NUM_STEPS + 1):
        print(f"{t:9d} | {solution[t, 0]:7.4f} | {solution[t, 1]:7.4f}")
   
    
    # Plot only the forecasted GDP (Y_t^(2))
    time_steps = np.arange(NUM_STEPS + 1)
    plt.figure(figsize=(8, 6))
    plt.plot(time_steps, solution[:, 1], 'r-', label='Forecasted GDP (Y_t^(2))')
    plt.title('Forecasted GDP Over Time')
    plt.xlabel('Time Step (t)')
    plt.ylabel('GDP Value')
    plt.grid(True)
    plt.legend()
    plt.show('gdp_forecast_plot.png')