import random


def create_random_dict():
    """
    Create a dictionary with random keys from 0, 1000
    and random value of keys from 0, 1000
    :return: dictionary
    """
    lower, upper = 0, 1000

    num_loop = random.randint(1, 1000)
    sample_dict = {
        random.randint(lower, upper): random.randint(lower, upper)
        for _ in range(num_loop)
    }

    return sample_dict
