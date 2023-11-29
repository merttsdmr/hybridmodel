import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the space
x_min, x_max = 0, 100
y_min, y_max = 0, 20
t_max = 50

# Create a grid of coordinates for the space
x, y = np.meshgrid(np.arange(x_min, x_max + 1), np.arange(y_min, y_max + 1))

# Initialize c(x, 0) using the given condition
c_x_0 = 0.5 * (np.heaviside(x - 40, 1) - np.heaviside(x - 60, 1))

# Generate random values for infectious individuals based on c(x, 0)
infectious_agents = np.random.rand(*c_x_0.shape) < c_x_0

# Create a figure for the initial distribution
plt.figure(figsize=(10, 5))
plt.scatter(x, y, c=infectious_agents, cmap='Reds', s=20, alpha=0.5, marker='o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Distribution of Infectious Individuals (I) at t=0')
plt.grid(True)
plt.show()

# Perform the time-stepping simulation
for t in range(1, t_max + 1):
    # Create a copy of the current state to avoid modifying it while iterating
    new_infectious_agents = infectious_agents.copy()
    
    # Loop through each location
    for i in range(x_max):
        for j in range(y_max):
            if infectious_agents[j, i]:
                # Implement your random walk rule here
                # Select a random neighbor and swap positions with them
                neighbor_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                np.random.shuffle(neighbor_offsets)
                for offset_x, offset_y in neighbor_offsets:
                    new_x, new_y = i + offset_x, j + offset_y
                    if 0 <= new_x < x_max and 0 <= new_y < y_max and not new_infectious_agents[new_y, new_x]:
                        # Swap positions
                        new_infectious_agents[j, i] = False
                        new_infectious_agents[new_y, new_x] = True
                        break
                    elif 0 <= new_x < x_max and new_y < 0:
                        # If agent hits the top boundary, move downwards
                        new_infectious_agents[j, i] = False
                        new_infectious_agents[j + 1, i] = True
                        break
                    elif 0 <= new_x < x_max and new_y >= y_max:
                        # If agent hits the bottom boundary, move upwards
                        new_infectious_agents[j, i] = False
                        new_infectious_agents[j - 1, i] = True
                        break
    
    # Update the infectious agents array
    infectious_agents = new_infectious_agents
    



    # Plot the updated distribution of infectious individuals
plt.figure(figsize=(10, 5))
plt.scatter(x, y, c=infectious_agents, cmap='Reds', s=20, alpha=0.5, marker='o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title(f'Distribution of Infectious Individuals (I) at t={t}')
plt.grid(True)
plt.show()