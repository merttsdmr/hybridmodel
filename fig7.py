import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the space
x_min, x_max = 0, 100
y_min, y_max = 0, 20
t_max = 500

# Create a grid of coordinates for the space
x, y = np.meshgrid(np.arange(x_min, x_max + 1), np.arange(y_min, y_max + 1))

# Initialize the position of a single agent
agent_x = np.random.randint(40, 60)
agent_y = np.random.randint(0, 20)

# Create an array to store the agent's position at each time step
agent_positions = [(agent_x, agent_y)]

# Perform the random walk simulation for the agent
for t in range(1, t_max + 1):
    # Select a random neighbor and update the agent's position
    neighbors = [(agent_x + 1, agent_y), (agent_x - 1, agent_y), (agent_x, agent_y + 1), (agent_x, agent_y - 1)]
    agent_x, agent_y = neighbors[np.random.randint(4)]  # Select a random neighbor
    
    # Make sure the agent stays within the boundaries
    agent_x = max(x_min, min(x_max, agent_x))
    agent_y = max(y_min, min(y_max, agent_y))
    
    agent_positions.append((agent_x, agent_y))

# Extract x and y coordinates of the agent at each time step
agent_x_coords, agent_y_coords = zip(*agent_positions)

# Plot the random walk of the agent
plt.figure(figsize=(10, 5))
plt.plot(agent_x_coords, agent_y_coords, marker='o', linestyle='-')
plt.plot(agent_x_coords[0], agent_y_coords[0], marker='o', markersize=8, color='orange', label='Start')
plt.plot(agent_x_coords[-1], agent_y_coords[-1], marker='o', markersize=8, color='red', label='End')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Random Walk of a Single Agent')
plt.legend()
plt.grid(True)
plt.show()
