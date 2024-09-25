
import random
from collections import defaultdict

def monte_carlo_sum_prob(args, num_simulations=1_000_000):
    # Dictionary to store frequencies of each sum
    sum_frequencies = defaultdict(int)

    # Perform Monte Carlo simulations
    for _ in range(num_simulations):
        # Randomly choose one number from each range (1 to arg)
        total_sum = sum(random.randint(1, arg) for arg in args)

        # Increment the frequency for the calculated sum
        sum_frequencies[total_sum] += 1

    # Calculate probabilities for each sum
    probabilities = {s: freq / num_simulations for s, freq in sum_frequencies.items()}

    return probabilities

# Example usage
args = [4, 6, 7]
probabilities = monte_carlo_sum_prob(args)

# Print the results
for total_sum, prob in sorted(probabilities.items()):
    print(f"Sum: {total_sum}, Probability: {prob*100:.6f}%")
