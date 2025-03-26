import numpy as np
import matplotlib.pyplot as plt


def simulate_SIR(vaccination_rate):
    # Calculate the number of vaccinated individuals (who cannot be infected)
    N = 10000, beta = 0.3, gamma = 0.05, time_steps = 1000
    V = int(N * vaccination_rate)
    # Adjust the susceptible count: total population minus vaccinated and one initial infected
    S = N - V - 1
    I = 1         # Initially infected
    R = 0         # Recovered individuals
    I_array = [I]

    # Pseudocode:
    # For each time step:
    #   1. Calculate infection probability: beta * (I/N)
    #   2. New infections are determined from the susceptible group using a binomial draw
    #   3. New recoveries are determined from the infected group using a binomial draw
    #   4. Update S, I, and R and record the infected count
    for t in range(time_steps):
        # Ensure S is non-negative
        if S < 0:
            S = 0
        else:
            p_infection = beta * (I / N)
            new_infections = np.random.binomial(S, p_infection)
            new_recoveries = np.random.binomial(I, gamma)
            S -= new_infections
            I += new_infections - new_recoveries
            R += new_recoveries

    # Calculate the infection probability (if S > 0)

    # Record the new values for plotting
        I_array.append(I)
    return I_array


plt.figure(figsize=(6, 4), dpi=150)
# Plot infected curves for different vaccination rates from 0% to 100%
for vacc in range(0, 110, 10):
    vacc_rate = vacc / 100.0
    I_array = simulate_SIR(vacc_rate)
    plt.plot(I_array, label=f'Vaccination {vacc}%')
plt.xlabel('Time')
plt.ylabel('Number of Infected')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.show()
plt.savefig("SIR_vaccination", type="png")
