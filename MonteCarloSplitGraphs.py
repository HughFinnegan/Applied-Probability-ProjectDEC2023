import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(n, total_trials=10000):
    net_payoffs = []
    running_averages = []

    for trial in range(1, total_trials + 1):
        random_numbers = np.random.uniform(0, 1, n)

        if all(1/n <= num <= 1 - 1/n for num in random_numbers):
            net_payoff = 10
        else:
            net_payoff = -1

        net_payoffs.append(net_payoff)

        running_average = np.mean(net_payoffs)
        running_averages.append(running_average)

    final_result = running_average  
    return net_payoffs, running_averages, final_result

n_values = [10, 100, 1000]
results = {}

plt.figure(figsize=(12, 8), facecolor='white') 

for i, n in enumerate(n_values):
    plt.subplot(len(n_values), 1, i+1)
    _, running_averages, final_result = monte_carlo_simulation(n) 
    plt.plot(range(1, len(running_averages) + 1), running_averages, linestyle='--', label=f'Running Avg (n = {n})')

    plt.text(0.8, 0.8, f'Final Result: {final_result:.2f}', transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')

plt.suptitle('Monte Carlo Simulation Results')
plt.xlabel('Number of Trials')

for i, n in enumerate(n_values):
    plt.subplot(len(n_values), 1, i+1)
    plt.ylabel('Running Average')
    plt.legend()

plt.tight_layout()
plt.show()
