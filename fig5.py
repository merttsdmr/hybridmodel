import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the space
x_min, x_max = 0, 100
y_min, y_max = 0, 20
t_max = 500

# Create a grid of coordinates for the space
x, y = np.meshgrid(np.arange(x_min, x_max + 1), np.arange(y_min, y_max + 1))

# Initialize c(x, 0) using the given condition
c_x_0 = 0.5 * (np.heaviside(x - 40, 1) - np.heaviside(x - 60, 1))

# Generate random values for infectious individuals based on c(x, 0)
infectious_agents = np.random.rand(*c_x_0.shape) < c_x_0
# Plot the initial distribution of infectious individuals
plt.figure(figsize=(10, 5))
plt.scatter(x, y, c=infectious_agents, cmap='Reds', s=20, alpha=0.5, marker='o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Distribution of Infectious Individuals (I) at t=0')
plt.grid(True)
plt.show()