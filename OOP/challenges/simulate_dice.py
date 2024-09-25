from collections import defaultdict
import itertools


def calculate_sum_probabilities(args):
    # Dictionary to store frequencies of each sum
    sum_frequencies = defaultdict(int)

    # Get all possible values for each argument
    ranges = [range(1, arg + 1) for arg in args]
    print(ranges)

    # Total number of possible combinations
    total_combinations = 1
    for arg in args:
        total_combinations *= arg
    print(total_combinations)

    # Generate all possible combinations and calculate sums
    # * means unpacking, itertools.product expects separate iterables, not a single list
    # itertools.product(*ranges) generates the Cartesian product of input iterables,
    # which means it produces all possible combinations of elements from the provided iterables.
    for combination in itertools.product(*ranges):
        sum_value = sum(combination)
        sum_frequencies[sum_value] += 1
    # below is some example showing it step by step
    ranges = [range(2), range(3)]
    print(*ranges)
    print(sum(range(1,10)))
    # Calculate the probabilities for each sum
    sum_probabilities = {s: freq / total_combinations for s, freq in sum_frequencies.items()}

    return sum_probabilities


# Example usage
args = [4, 6, 7]
probabilities = calculate_sum_probabilities(args)

# Print the result
for sum_value, probability in sorted(probabilities.items()):
    print(f"Sum: {sum_value}, Probability: {probability*100:.6f}%")
