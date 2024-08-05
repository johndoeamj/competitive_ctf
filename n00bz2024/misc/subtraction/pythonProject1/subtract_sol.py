import random
import time
import numpy as np
from collections import Counter

# Seed the random number generator for reproducibility
x = time.time()
# x = 1722777799.456309
print("x: ", x)
random.seed(x)

# Initialize the list with random even integers
n = 696969
a = [random.randint(0, n) for _ in range(n)]
a = [x - (x % 2) for x in a]  # Ensure all numbers are even


def get_median(lst):
    return round(np.median(lst))


def get_mode(lst):
    counts = Counter(lst)
    return round(counts.most_common(1)[0][0])


def get_mean(lst):
    return round(np.mean(lst))


def update_list(a, c):
    return [abs(c - x) for x in a]

prev_len = -1
special = False
for iteration in range(20):

    c = get_median(a)

    if len(set(update_list(a,c))) <= prev_len + 10:

        c = round(max(a)//2)

    # Update the list according to the rule
    a = update_list(a, c)

    prev_len = len(set(a))

    # Print status
    current_len_set = len(set(a))
    print(f'Attempt {iteration + 1}: Len: {current_len_set}')

    # Check if all elements are the same
    if current_len_set == 1:
        print("win")
        break

else:
    print("Failed to converge to a single value within 20 iterations.")
    print(set(a))
