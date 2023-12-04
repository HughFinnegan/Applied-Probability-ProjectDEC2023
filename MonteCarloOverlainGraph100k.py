import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(n, total_trials=100000):
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

    return running_averages

n_values = [10, 100, 1000]

plt.figure(figsize=(12, 6), facecolor='white')

for n in n_values:
    running_averages = monte_carlo_simulation(n)  
    plt.plot(range(1, len(running_averages) + 1), running_averages, label=f'Running Avg (n = {n})')

    equation_text = f'For N = {n}, RunAvg = {running_averages[-1]:.2f}'
    plt.text(0.99, 0.8 - n_values.index(n) * 0.04, equation_text, transform=plt.gca().transAxes, ha='right', va='center', fontsize=10)

plt.title('Monte Carlo Simulation Results - Running Averages')
plt.xlabel('Number of Trials')
plt.ylabel('Running Average')
plt.legend()
plt.show()
