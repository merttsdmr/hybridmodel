import numpy as np
import random
import matplotlib.pyplot as plt

# Parameters
L = 100  # Width of the lattice
H = 100  # Height of the lattice
b = 0.125  # Infection rate
c = 0.0  # Recovery rate (no recovery)
initial_infectious_fraction = 0.1  # Initial fraction of infectious agents
max_steps = 15

# Function to calculate I(t) at time t
def calculate_I(t):
    I_0 = 0.1
    beta_t = b * t
    return I_0 * np.exp(beta_t) / (1 + I_0 * (np.exp(beta_t) - 1))

# Lists to store the number of infectious agents at each time point
infectious_counts = []
times=[0,7,15]
# Simulation
for t in range(max_steps+1):
    # Calculate I(t)
    current_I = int(calculate_I(t) * L * H)
    
    # Generate random positions for infectious agents
    infectious_agents = [
        (random.randint(0, L - 1), random.randint(0, H - 1))
        for _ in range(current_I)
    ]
    cm = plt.cm.Reds
    cm.set_under('white')
    if t == 0 or t == 7 or t==15: 
    # Create a plot to visualize the infectious agents
        plt.figure(figsize=(6, 6))
        plt.imshow(np.zeros((H, L), dtype=int), cmap=cm, interpolation='none', origin='upper', vmin=0, vmax=1)
        plt.scatter(*zip(*infectious_agents), marker='.', c='red', s=5)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title(f"Infectious Agents at Time Step {t}")
        plt.show()
