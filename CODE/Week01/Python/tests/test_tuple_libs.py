"""
Testing cases of method and function of TUPLE
"""

import random
from libs.create_tuple import create_random_tuple


# =============================================================================


def test_tuple_count():
    """
    Test tuple.count(val):
        - Return quantity of all elements have val
    """
    num_test = 10

    for _ in range(num_test):
        tpl, _ = create_random_tuple()

        element = random.choice(tpl)

        count_returned = tpl.count(element)
        num_element = 0
        for elem in tpl:
            if elem == element:
                num_element += 1

        assert count_returned == num_element


# =============================================================================


def test_tuple_index():
    """
    Test tuple.index(val, start, end):
        - first index of element in list[start:end] has value
    """
    num_test = 10

    for _ in range(num_test):
        tpl, len_tuple = create_random_tuple()

        point_start = random.randint(0, len_tuple - 2)
        point_end = random.randint(point_start + 1, len_tuple - 1)

        element = random.choice(list(tpl[point_start:point_end]))

        idx_returned = tpl.index(element, point_start, point_end)
        idx = point_start
        while tpl[idx] != element:
            idx += 1

        assert idx_returned == idx


# =============================================================================


def test_tuple_all():
    """
    Test function all(tuple):
        - (any elements in tuple = False) == False
        - (all elements in tuple = True) == True
    """
    num_test = 10

    for _ in range(num_test):
        tpl, _ = create_random_tuple()

        returned_val = all(tpl)

        test_val = True
        for elem in tpl:
            test_val = bool(elem)
            if not test_val:
                break

        assert test_val == returned_val


# =============================================================================


def test_tuple_any():
    """
    Test function any(tuple):
        - (any elements in tuple = True) == True
    """
    num_test = 10

    for _ in range(num_test):
        tpl, _ = create_random_tuple()

        returned_val = any(tpl)

        test_val = False
        for elem in tpl:
            test_val = bool(elem)
            if test_val:
                break

        assert test_val == returned_val


# =============================================================================


def test_tuple_enumerate():
    """
    Test function enumerate(tuple):
        - [(0, value_0), (1, value_1), (2, value_2), ...]
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        tpl, len_tuple = create_random_tuple()

        val_start = random.randint(lower, upper)
        enumerate_tpl = list(enumerate(tpl, start=val_start))

        test_val = True
        for i in range(len_tuple):
            if enumerate_tpl[i][1] != tpl[enumerate_tpl[i][0] - val_start]:
                test_val = False
                break

        assert test_val


# =============================================================================


def test_tuple_len():
    """
    Test function len(tuple):
        - Return length of tuple
    """
    num_test = 10

    for _ in range(num_test):
        tpl, len_tuple = create_random_tuple()

        assert len_tuple == len(tpl)


# =============================================================================


def test_tuple_max():
    """
    Test function max(tuple):
        - Return the maximum value of element in tuple
    """
    num_test = 10

    for _ in range(num_test):
        tpl, len_tuple = create_random_tuple()

        max_element = max(tpl)

        max_test = tpl[0]
        for i in range(len_tuple):
            if max_test < tpl[i]:
                max_test = tpl[i]

        assert max_element == max_test


# =============================================================================


def test_tuple_min():
    """
    Test function min(tuple):
        - Return the minimum value of element in tuple
    """
    num_test = 10

    for _ in range(num_test):
        tpl, len_tuple = create_random_tuple()

        min_element = min(tpl)

        min_test = tpl[0]
        for i in range(len_tuple):
            if min_test > tpl[i]:
                min_test = tpl[i]

        assert min_element == min_test


# =============================================================================


def test_tuple_sum():
    """
    Test function sum(tuple, value):
        - tuple[0] + tuple[1] + ... + tuple[-1] + value == sum(tuple)
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        tpl, _ = create_random_tuple()

        val_start = random.randint(lower, upper)
        sum_of_tpl = sum(tpl, start=val_start)

        sum_test = val_start
        for elem in tpl:
            sum_test += elem

        assert sum_test == sum_of_tpl
