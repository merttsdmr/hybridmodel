import numpy as np
import matplotlib.pyplot as plt
import math
# Parameters
I_0 = 0.1
max_t = 20
beta_values = [0.125, 0.25, 0.5, 1]

# Function to calculate I(t) at time t for a given β
def calculate_I(t, beta):
    return I_0 * np.exp(beta * t) / (1 + I_0 * (np.exp(beta * t) - 1))

# Agent-Based Simulation
L = 100  # Width of the lattice
H = 100  # Height of the lattice
c = 0.0  # Recovery rate set to zero
initial_infectious_fraction = 0.01  # Initial fraction of infectious agents
max_steps = 16

# Function to perform agent-based simulation for ratio calculation
def agent_based_simulation_ratio(L, H, b, c,  max_steps):
    total_agents = L * H
    infectious_counts = []
    for step in range(max_steps):

    # Calculate the current fraction of infectious agents based on I(t)
        current_infectious =math.floor( I_0 * np.exp(beta * step) / (1 + I_0 * (np.exp(beta * step) - 1)) * L*H)
        infectious_counts.append(current_infectious / total_agents)
    return infectious_counts



# Create a single figure
plt.figure(figsize=(10, 6))

# Plot I(t) for different beta values
for beta in beta_values:
    t = np.arange(0, max_t + 1)
    I = calculate_I(t, beta)
    plt.plot(t, I, label=f'β = {beta}')
# Run agent-based simulation and plot the ratio with discrete points
for beta in beta_values:
    ratio = agent_based_simulation_ratio(L, H, beta, c, max_steps)
    t = np.arange(0, max_steps)
    plt.scatter(t, ratio, label=f'Agent-Based Ratio (β = {beta}', marker='o')  # marker='o' for discrete points

# Set the x-axis limits to 0 and 15
plt.xlim(0, 15)

plt.xlabel("Time (t)")
plt.ylabel("Proportion of Infectious Agents (I(t)) / Ratio of Infectious Agents in Society")
plt.title("Infectious Agents and Agent-Based Simulation for Different β Values (0-15 Time Interval)")
plt.grid()
plt.legend()

plt.show()






