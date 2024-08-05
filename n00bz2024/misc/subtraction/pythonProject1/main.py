import random

# Initialize parameters
n = 696969
a = []

# Generate the initial array with even integers
for i in range(n):
    a.append(random.randint(0, n))
    a[i] -= a[i] % 2

# Function to calculate the median of an array
def calculate_median(array):
    sorted_array = sorted(array)
    mid_index = len(sorted_array) // 2
    if len(sorted_array) % 2 == 0:
        return (sorted_array[mid_index - 1] + sorted_array[mid_index]) // 2
    else:
        return sorted_array[mid_index]

# Simulate the interaction process
for turns in range(50
                   ):
    # Calculate the current median value in the array
    median_a = calculate_median(a)

    c = median_a
    print(f'Turn {turns + 1}, input: {c}, setLen: {len(set(a))}')

    # Apply the transformation to the array
    for i in range(n):
        a[i] = abs(c - a[i])

    # Check if all elements are the same
    if len(set(a)) == 1:
        print("Flag condition met! All elements are the same.")
        break

# In a real scenario, this is where the server would return the flag
# For now, we simulate this step
if len(set(a)) == 1:
    print("Simulated flag: FLAG{example_flag_value}")
