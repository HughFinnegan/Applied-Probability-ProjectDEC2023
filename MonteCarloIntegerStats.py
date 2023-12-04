import numpy as np

def monte_carlo_simulation(n, total_trials=10000):
    net_payoffs = []

    for _ in range(total_trials):
        random_numbers = np.random.uniform(0, 1, n)
        
        if all(1/n <= num <= 1 - 1/n for num in random_numbers):
            net_payoff = 10
        else:
            net_payoff = -1

        net_payoffs.append(net_payoff)

    average_net_payoff = np.mean(net_payoffs)

    return average_net_payoff

n_values = [10, 100, 1000]
results = {}

for n in n_values:
    expected_payoff = monte_carlo_simulation(n)
    results[n] = expected_payoff

for n in n_values:
    print(f"Expected Net Payoff for n = {n}: {results[n]}")
