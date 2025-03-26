import numpy as np
import matplotlib.pyplot as plt

# Parameters for the spatial model
grid_size = 100   # Size of the grid (100x100)
beta = 0.3        # Probability of infection to a neighbor
gamma = 0.05      # Recovery probability per time step
time_steps = 100  # Number of time steps

# Initialize the grid: all individuals are susceptible (0)
population = np.zeros((grid_size, grid_size), dtype=int)

# Randomly select a cell for the initial outbreak and set it as infected (1)
x = np.random.randint(0, grid_size)
y = np.random.randint(0, grid_size)
population[x, y] = 1


def plot_grid(grid, time_step):
    """Plot the grid as a heatmap where:
       0: Susceptible, 1: Infected, 2: Recovered"""
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(grid, cmap='viridis', interpolation='nearest')
    plt.title(f'Time Step {time_step}')
    cbar = plt.colorbar(ticks=[0, 1, 2])
    cbar.set_label('State (0: Susceptible, 1: Infected, 2: Recovered)')
    plt.clim(-0.5, 2.5)
    plt.show()

# Pseudocode:
# For each time step:
#   1. Create a copy of the current grid to update the state
#   2. For every cell that is infected:
#       a. For each of its 8 neighbors:
#            - Check if the neighbor is within the grid boundaries
#            - If the neighbor is susceptible, infect it with probability beta
#       b. The infected cell recovers with probability gamma
#   3. Replace the old grid with the updated grid
#   4. Plot the grid at selected time steps (e.g., t=10, 50, 100)


# Plot the initial state
plot_grid(population, 0)

for t in range(1, time_steps + 1):
    new_population = population.copy()  # Copy current grid to update states
    # Find indices of all currently infected cells
    infected_indices = np.argwhere(population == 1)
    for idx in infected_indices:
        i, j = idx
        # Check all 8 neighbors around the cell
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue  # Skip the cell itself
                ni, nj = i + di, j + dj
                # Check if neighbor is within the grid boundaries
                if ni < 0 or ni >= grid_size or nj < 0 or nj >= grid_size:
                    continue
                # If the neighbor is susceptible, infect it with probability beta
                if population[ni, nj] == 0 and np.random.rand() < beta:
                    new_population[ni, nj] = 1
        # Infected cell may recover with probability gamma
        if np.random.rand() < gamma:
            new_population[i, j] = 2
    population = new_population
    # Plot the grid at specific time steps (e.g., 10, 50, 100)
    if t in [10, 50, 100]:
        plot_grid(population, t)
