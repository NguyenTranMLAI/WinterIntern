import random


def create_random_list():
    """
    Create a list with random length from 1 to 1000
    and random value of elements from 0, 1000
    :return: list, length of list
    """
    lower, upper = 0, 1000
    max_len_list = 1000

    len_list = random.randint(1, max_len_list)
    lst = [random.randint(lower, upper) for _ in range(len_list)]

    return lst, len_list
