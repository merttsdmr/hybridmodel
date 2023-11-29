import numpy as np
import matplotlib.pyplot as plt
import itertools

# Define the dimensions of the space
x_min, x_max = 0, 100
y_min, y_max = 0, 20
t_max = 500
D = 0.25  # Diffusion coefficient

# Create a grid of coordinates for the space
x, y = np.meshgrid(np.arange(x_min, x_max + 1), np.arange(y_min, y_max + 1))

# Initialize c(x, 0) using the given condition
c_x_0 = 20 * 0.5 * (np.heaviside(x - 40, 1) - np.heaviside(x - 60, 1))

# Generate random values for infectious individuals based on c(x, 0)
infectious_agents = np.random.rand(*c_x_0.shape) < c_x_0

c_x_t_values = np.zeros((25, x_max - x_min + 1, t_max + 1))

# Perform the time-stepping simulation for 25 realizations
for N in range(25):
    infectious_agents = np.random.rand(*c_x_0.shape) < c_x_0
    
    for t in range(t_max + 1):
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
        
        # Store the c(x, t) values for this realization and time step
        c_x_t_values[N, :, t] = np.mean(infectious_agents, axis=0)

# Calculate the average c(x, t) values across realizations
c_x_t_avg = np.mean(c_x_t_values, axis=0)
c_x_t_percentile25=np.percentile(c_x_t_values,25,axis=0)
c_x_t_percentile75=np.percentile(c_x_t_values,75,axis=0)
# Plot the average c(x, t) values as a function of both x and t
plt.figure(figsize=(10, 5))

x_values = range(101)

t_colors = {
    10: "r",
    100: "g",
    500: "b",
}

for i in [10, 100, 500]:
    plt.plot(x_values, c_x_t_avg[:, i], linestyle='--', label=f'mean t = {i}', color=t_colors[i])
    plt.plot(x_values,c_x_t_percentile25[:,i],linestyle=':', label=f'0.25p t = {i}', color=t_colors[i])
    plt.plot(x_values,c_x_t_percentile25[:,i],linestyle=':', label=f'p.75p t = {i}', color=t_colors[i])
    plt.fill_between(x_values, c_x_t_percentile25[:,i], c_x_t_percentile75[:,i], color=t_colors[i], alpha=0.2)
t = range(t_max + 1)
x = range(x_max + 1)

# Initialize the solution matrix
I = np.zeros((len(x), len(t)))

# Set the initial condition I(x, 0) = 0.1
I[40:60, 0] = 0.5

# Solve the diffusion equation numerically using finite differences
for n in range(0, len(t) - 1):
    for i in range(1, len(x) - 1):
        I[i, n + 1] = I[i, n] + 0.25 * (I[i + 1, n] - 2 * I[i, n] + I[i - 1, n])

# Plot the solution
for i in [10, 100, 500]:
    
    plt.plot(x, I[:, i], linestyle='-', label=f't = {i}', color=t_colors[i])

plt.xlabel('X Coordinate')
plt.ylabel('Proportion')
plt.title('Comparison between Ih and Diffusion Equation Solution')
plt.grid(True)
plt.legend()
plt.show()
