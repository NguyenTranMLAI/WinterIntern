import random


def create_random_tuple():
    """
    Create a tuple with random length from 1 to 1000
    and random value of elements from 0, 1000
    :return: tuple, length of tuple
    """
    lower, upper = 0, 1000
    max_len_list = 1000

    len_tuple = random.randint(1, max_len_list)
    tpl = tuple(random.randint(lower, upper) for _ in range(len_tuple))

    return tpl, len_tuple
