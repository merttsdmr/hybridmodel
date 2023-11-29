import numpy as np
import matplotlib.pyplot as plt

# Define model parameters
D = 0.25
beta = 0.1
L = 100
H = 20
t_max = 100

# Define the dimensions of the space
x_min, x_max = 0, L
y_min, y_max = 0, H

# Create a grid of coordinates for the space
x, y = np.meshgrid(np.arange(x_min, x_max + 1), np.arange(y_min, y_max + 1))

# Initialize c(x, 0) using the given condition
c_x_0 = 0.5 * (np.heaviside(x - 40, 1) - np.heaviside(x - 60, 1))

# Generate random values for infectious individuals based on c(x, 0)
infectious_agents = np.random.rand(*c_x_0.shape) < c_x_0

# Function to simulate infection spread
def simulate_infection(infectious_agents, D, beta, t_max):
    for t in range(t_max):
        new_infectious_agents = infectious_agents.copy()
        for i in range(1, L):
            for j in range(1, H):
                if infectious_agents[j,i]:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx != 0 or dy != 0:
                                x_new, y_new = i + dx, j + dy
                                if 0 <= x_new < L and 0 <= y_new < H and not infectious_agents[y_new, x_new]:
                                    # Calculate transmission probability
                                    transmission_prob = beta
                                    if dx != 0 and dy != 0:
                                        transmission_prob /= 2
                                    if np.random.rand() < transmission_prob:
                                        new_infectious_agents[y_new, x_new] = True
        infectious_agents = new_infectious_agents.copy()

    return infectious_agents

# Simulate infection spread
final_infectious_agents = simulate_infection(infectious_agents, D, beta, t_max)

# Plot the final distribution of infectious individuals
plt.figure(figsize=(10, 5))
plt.scatter(x, y, c=final_infectious_agents, cmap='Reds', s=20, alpha=0.5, marker='o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Distribution of Infectious Individuals (I) at t=100')
plt.grid(True)
plt.show()
