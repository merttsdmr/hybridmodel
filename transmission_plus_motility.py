import numpy as np
import matplotlib.pyplot as plt
import random
# Parameters
beta = 0.1
L = 100
H = 20
x_min, x_max = 0, 100
y_min, y_max = 0, 20
t_max = 105
D = 0.25  # Diffusion coefficient

# Create a grid of coordinates for the space
x, y = np.meshgrid(np.arange(x_min, x_max + 1), np.arange(y_min, y_max + 1))

# Initialize c(x, 0) using the given condition
c_x_0 =0.5 * (np.heaviside(x - 40, 1) - np.heaviside(x - 60, 1))

# Generate random values for infectious individuals based on c(x, 0)

c_x_t_values10 = np.zeros(( 25, x_max - x_min + 1))
c_x_t_values30 = np.zeros(( 25, x_max - x_min + 1))
c_x_t_values100 = np.zeros(( 25, x_max - x_min + 1))
# Perform the time-stepping simulation for 25 realizations

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
for N in range(25):
# Simulate infection spread
    final_infectious_agents10 = simulate_infection(infectious_agents, D, beta,10)
    avg_final_infectious_agents10=np.mean(final_infectious_agents10,axis=0)
    final_infectious_agents30 = simulate_infection(infectious_agents, D, beta, 30)
    avg_final_infectious_agents30=np.mean(final_infectious_agents30,axis=0)
    final_infectious_agents100 = simulate_infection(infectious_agents, D, beta, 100)
    avg_final_infectious_agents100=np.mean(final_infectious_agents100,axis=0)
    c_x_t_values10[N,:] = avg_final_infectious_agents10
    c_x_t_values30[N,:] = avg_final_infectious_agents30
    c_x_t_values100[N,:] = avg_final_infectious_agents100
c_x_t_25_percentile10=np.percentile(c_x_t_values10,25,axis=0)
c_x_t_75_percentile10=np.percentile(c_x_t_values10,75,axis=0)
c_x_t_avg10=np.mean(c_x_t_values10,axis=0)
c_x_t_25_percentile30=np.percentile(c_x_t_values30,25,axis=0)
c_x_t_75_percentile30=np.percentile(c_x_t_values30,75,axis=0)
c_x_t_avg30=np.mean(c_x_t_values30,axis=0)
c_x_t_25_percentile100=np.percentile(c_x_t_values100,25,axis=0)
c_x_t_75_percentile100=np.percentile(c_x_t_values100,75,axis=0)
c_x_t_avg100=np.mean(c_x_t_values100,axis=0)
# Plot the average c(x, t) values as a function of both x and t
plt.figure(figsize=(10, 5))

x_values = range(101)


t_colors = {
    10: "r",
    30: "g",
    100: "b",
}
plt.plot(x_values,c_x_t_25_percentile10, linestyle=':', label=f'0.25 percentile t = 10', color="r")
plt.plot(x_values,c_x_t_75_percentile10, linestyle=':', label=f'0.75 percentile t = 10', color="r")
plt.plot(x_values,c_x_t_25_percentile30, linestyle=':', label=f'0.25 percentile t = 30', color="g")
plt.plot(x_values,c_x_t_75_percentile30, linestyle=':', label=f'0.75 percentile t = 30', color="g")
plt.plot(x_values,c_x_t_25_percentile100, linestyle=':', label=f'0.25 percentile t = 100', color="b")
plt.plot(x_values,c_x_t_75_percentile100, linestyle=':', label=f'0.75 percentile t = 100', color="b")
plt.plot(x_values,c_x_t_avg30, linestyle='--', label=f't = 30', color="g")
plt.plot(x_values,c_x_t_avg100, linestyle='--', label=f't = 100', color="b")
plt.plot(x_values,c_x_t_avg10, linestyle='--', label=f't = 10', color="r")
plt.plot(x_values,c_x_t_avg30, linestyle='--', label=f't = 30', color="g")
plt.plot(x_values,c_x_t_avg100, linestyle='--', label=f't = 100', color="b")
plt.fill_between(x_values, c_x_t_25_percentile10, c_x_t_75_percentile10, color="r", alpha=0.2)
plt.fill_between(x_values, c_x_t_25_percentile30, c_x_t_75_percentile30, color="g", alpha=0.2)
plt.fill_between(x_values, c_x_t_25_percentile100, c_x_t_75_percentile100, color="b", alpha=0.2)

t = range(t_max + 1)
x = range(x_max + 1)

# Initialize the solution matrix
I = np.zeros((len(x), len(t)))

# Set the initial condition I(x, 0) = 0.5
I[40:60, 0] = 0.5
alpha = 0.1

# Solve the diffusion equation numerically using finite differences
for n in range(0, len(t) - 1):
    for i in range(1, len(x) - 1):
        I[i, n + 1] = I[i, n] + 0.25 * (I[i + 1, n] - 2 * I[i, n] + I[i - 1, n])+alpha * I[i, n] * (1 - I[i, n])

# Plot the solution
for i in [10, 30, 100]:
    plt.plot(x, I[:, i], linestyle='-', label=f't = {i}', color=t_colors[i])


plt.xlabel('X Coordinate')
plt.ylabel('Proportion')
plt.title('Comparison between Ih and Fisher Equation Solution')
plt.grid(True)
plt.legend()
plt.show()

