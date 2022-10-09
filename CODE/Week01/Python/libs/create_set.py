import random


def create_random_set():
    """
    Create a set with random value of elements from 0, 1000
    :return: set
    """
    lower, upper = 0, 1000

    num_loop = random.randint(1, 1000)
    sample_set = {random.randint(lower, upper) for _ in range(num_loop)}

    return sample_set
