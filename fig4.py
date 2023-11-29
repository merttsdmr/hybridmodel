import numpy as np
import random
import matplotlib.pyplot as plt

# Parameters
L = 100  # Width of the lattice
H = 100  # Height of the lattice
b = 0.5  # Infection rate
c = 0.0  # Recovery rate (no recovery)
initial_infectious_fraction = 0.015  # Initial fraction of infectious agents
max_steps = 15

# Function to calculate I(t) at time t
def calculate_I(t):
    I_0 = 0.1
    beta_t = b * t
    return I_0 * np.exp(beta_t) / (1 + I_0 * (np.exp(beta_t) - 1))

# Lists to store the number of infectious agents at each time step
infectious_counts = []

# Define the size of each sub-society and the gap between them
sub_society_size = 20
gap = 5

# Create a lattice to represent agents (0: susceptible, 1: infectious)
lattice = np.zeros((H, L), dtype=int)

# Initialize infectious agents based on the initial condition
current_I = int(initial_infectious_fraction * L * H)

# Define positions for the four sub-societies near the corners
sub_societies = [
    ((gap, gap, gap + sub_society_size, gap + sub_society_size)),
    ((gap, H - gap - sub_society_size, gap + sub_society_size, H - gap)),
    (L - gap - sub_society_size, gap, L - gap, gap + sub_society_size),
    (L - gap - sub_society_size, H - gap - sub_society_size, L - gap, H - gap)
]

# Initialize infectious agents in each sub-society
infectious_agents = []
for sub_society in sub_societies:
    x1, y1, x2, y2 = sub_society
    sub_society_agents = [
        (random.randint(x1, x2), random.randint(y1, y2))
        for _ in range(current_I // 4)
    ]
    infectious_agents.extend(sub_society_agents)

for agent in infectious_agents:
    x, y = agent
    lattice[y, x] = 1

# Agent-based simulation
for t in range(max_steps + 1):  # Extend the simulation by one more time step
    # Store the current count of infectious agents
    infectious_counts.append(np.sum(lattice))

    if t == 0 or t == 7 or t==15:  # Check if it's t=0 or t=7
        # Plot the results for t=0 and t=7
        plt.figure(figsize=(6, 6))
        plt.imshow(lattice, cmap='Reds', interpolation='none', origin='upper', vmin=0, vmax=1)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title(f"Infectious Agents at Time Step {t}")
        plt.show()

    # Define lists to keep track of new infections and recoveries
    new_infections = []
    recoveries = []

    for y in range(H):
        for x in range(L):
            if lattice[y, x] == 1:
                # Agent is infectious
                neighbors = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if 0 <= x + dx < L and 0 <= y + dy < H]
                for neighbor_x, neighbor_y in neighbors:
                    if lattice[neighbor_y, neighbor_x] == 0 and random.random() < 0.1:
                        # Infect the susceptible neighbor with a probability of 0.1
                        new_infections.append((neighbor_x, neighbor_y))
                # Random recovery with a probability of 0.01
                if random.random() < 0.01:
                    recoveries.append((x, y))

    # Update the lattice with new infections and recoveries
    for x, y in new_infections:
        lattice[y, x] = 1
    for x, y in recoveries:
        lattice[y, x] = 0

# Plot the number of infectious agents over time (excluding t=0 and t=7)
plt.figure(figsize=(10, 6))
plt.plot(range(max_steps + 1), infectious_counts, marker='o', linestyle='-', color='blue')
plt.xlabel("Time Step")
plt.ylabel("Number of Infectious Agents")
plt.title("Number of Infectious Agents Over Time (Excluding t=0 and t=7)")
plt.grid()
plt.show()
