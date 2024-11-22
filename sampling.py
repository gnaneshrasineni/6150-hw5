import numpy as np

# Define the population and probabilities
population_size = 1000000
probabilities = [0.35, 0.4, 0.25]  # Probabilities for +1, -1, 0
#votes = np.random.choice([1, -1, 0], size=population_size, p=probabilities)
sample_sizes = [10, 120, 250, 320]

def simulate_majority_probability(sample_size, num_experiments=200):
    majority_count = 0
    for _ in range(num_experiments):
        # Generate a sample directly based on probabilities
        sample = np.random.choice([1, -1, 0], size=sample_size, p=probabilities)
        counts = np.bincount(sample + 1, minlength=3)  # Shift indices for -1, 0, 1
        if counts[0] > max(counts[1], counts[2]):  # -1 is majority
            majority_count += 1
    return majority_count / num_experiments

# Perform experiments for the given sample sizes
results = {size: simulate_majority_probability(size) for size in sample_sizes}

# Find the sample size for a probability of 0.9
def find_sample_size(target_probability=0.9, num_experiments=200, max_sample_size=5000):
    for sample_size in range(10, max_sample_size, 10):
        probability = simulate_majority_probability(sample_size, num_experiments)
        if probability >= target_probability:
            return sample_size
    return None  # Return None if the sample size is not found within the range

# Find the sample size for a probability of 0.9
required_sample_size = find_sample_size()

print(results)
print(required_sample_size)
