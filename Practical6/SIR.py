import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000            # Total population
beta = 0.3           # Infection rate per contact
gamma = 0.05         # Recovery probability per time step
time_steps = 1000    # Number of time steps

# Initial conditions
# Susceptible individuals (everyone except the initially infected)
S = N - 1
I = 1                # Initially infected individual
R = 0                # Recovered individuals

# Arrays to record the numbers over time
S_array = [S]
I_array = [I]
R_array = [R]

# Pseudocode:
# For each time step:
#   1. Calculate the infection probability per susceptible as beta * (I/N)
#   2. Determine new infections using a binomial distribution from S with probability p_infection
#   3. Determine new recoveries using a binomial distribution from I with probability gamma
#   4. Update S, I, and R accordingly
#   5. Record the updated S, I, R values

for t in range(time_steps):
    # Calculate infection probability for each susceptible
    p_infection = beta * (I / N)

    # Determine number of new infections from the susceptible population
    new_infections = np.random.binomial(S, p_infection)

    # Determine number of recoveries from the infected population
    new_recoveries = np.random.binomial(I, gamma)

    # Update the counts for susceptible, infected, and recovered
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    # Record the new values for plotting
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

# Plot the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_array, label='Susceptible')
plt.plot(I_array, label='Infected')
plt.plot(R_array, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR Model Simulation')
plt.legend()
plt.show()
plt.savefig('SIR', type='png')
