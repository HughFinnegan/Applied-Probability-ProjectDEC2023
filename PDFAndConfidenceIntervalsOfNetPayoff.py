import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import t
from scipy.stats import sem

sns.set(style="whitegrid")

def monte_carlo_simulation(n, total_trials=10000):
    net_payoffs = []

    for trial in range(1, total_trials + 1):
        random_numbers = np.random.uniform(0, 1, n)

        if all(1/n <= num <= 1 - 1/n for num in random_numbers):
            net_payoff = 10
        else:
            net_payoff = -1

        net_payoffs.append(net_payoff)

    final_result = np.mean(net_payoffs) 
    return net_payoffs, final_result

n_values = [10, 100, 1000]
results = {}

plt.figure(figsize=(15, 8), facecolor='white') 

for i, n in enumerate(n_values):
    net_payoffs, final_result = monte_carlo_simulation(n)

    data = net_payoffs
    ci = t.interval(0.95, len(data) - 1, loc=np.mean(data), scale=sem(data))
    sns.kdeplot(data, label=f'PDF (n = {n})')
    plt.fill_betweenx(y=[0, 0.1], x1=ci[0], x2=ci[1], alpha=0.3, color='red', label=f'95% CI (n = {n})')

    plt.text(1, 0.75 - 0.025 * i, f'95% CI (n = {n}): [{ci[0]:.2f}, {ci[1]:.2f}]', transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', ha='right')

plt.title('PDF and 95% Confidence Intervals of Net Payoffs')
plt.xlabel('Net Payoff')
plt.ylabel('Density')
plt.legend()
plt.show()
