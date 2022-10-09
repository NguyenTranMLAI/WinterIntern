"""
Testing cases of method and function of LIST
"""

import random
from libs.create_list import create_random_list


# =============================================================================


def test_list_append():
    """
    Test: list.append(val)
        - new_len == old_len + 1
        - list[-1] == val
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        lst, len_list = create_random_list()

        new_element = random.randint(lower, upper)
        lst.append(new_element)

        assert len(lst) == len_list + 1
        assert lst[-1] == new_element


# =============================================================================


def test_list_extend():
    """
    Test list_2.extend(list_1):
        - new_len_list_2 == old_len_list_2 + old_len_list_1
        - list_2[old_len_list_2:] == list_1
    """
    num_test = 10

    for _ in range(num_test):
        lst1, len_list_1 = create_random_list()
        lst2, len_list_2 = create_random_list()

        lst2.extend(lst1)

        assert len(lst2) == len_list_2 + len_list_1
        assert lst2[len_list_2:] == lst1


# =============================================================================


def test_list_insert():
    """
    Test list.insert(idx, val):
        - new_len == old_len + 1
        - new_list[idx] == val
        - new_list[:idx] == old_list[:idx] va new_list[idx+1:] = old_list[idx:]
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        old_lst, len_list = create_random_list()
        new_lst = old_lst[:]

        new_element = random.randint(lower, upper)
        idx = random.randint(1, upper)
        new_lst.insert(idx, new_element)

        assert len(new_lst) == len(old_lst) + 1
        if idx < len_list:
            assert new_lst[idx] == new_element
            assert (
                new_lst[:idx] == old_lst[:idx] and new_lst[idx + 1 :] == old_lst[idx:]
            )
        else:
            assert new_lst[-1] == new_element


# =============================================================================


def test_list_remove():
    """
    Test list.remove(elem)
        - new_len == old_len - 1
        - delete element of list
    """
    num_test = 10

    for _ in range(num_test):
        old_lst, _ = create_random_list()
        new_lst = old_lst[:]

        element = random.choice(old_lst)
        idx = old_lst.index(element)
        new_lst.remove(element)

        assert len(new_lst) == len(old_lst) - 1
        assert new_lst[:idx] == old_lst[:idx] and new_lst[idx:] == old_lst[idx + 1 :]


# =============================================================================


def test_list_pop():
    """
    Test list.pop(idx):
        - new_len == old_len - 1
        - old_list[idx] == old_list.pop(idx)
    """
    num_test = 10

    for _ in range(num_test):
        lst, len_list = create_random_list()

        idx = random.randint(0, len_list - 1)
        del_val = lst[idx]

        returned_val = lst.pop(idx)

        assert len(lst) == len_list - 1
        assert del_val == returned_val


# =============================================================================


def test_list_clear():
    """
    Test list.clear():
        - len_list == 0
    """
    num_test = 10

    for _ in range(num_test):
        lst, _ = create_random_list()

        lst.clear()

        assert len(lst) == 0


# =============================================================================


def test_list_index():
    """
    Test list.index(val, start, end):
        - first index of element in list[start:end] has value
    """
    num_test = 10

    for _ in range(num_test):
        lst, len_list = create_random_list()

        point_start = random.randint(0, len_list - 2)
        point_end = random.randint(point_start + 1, len_list - 1)

        element = random.choice(lst[point_start:point_end])

        returned_idx = lst.index(element, point_start, point_end)
        idx = point_start
        while lst[idx] != element:
            idx += 1

        assert returned_idx == idx


# =============================================================================


def test_list_count():
    """
    Test list.count(val):
        - Return quantity of all elements have val
    """
    num_test = 10

    for _ in range(num_test):
        lst, _ = create_random_list()
        element = random.choice(lst)

        returned_count = lst.count(element)
        num_element = 0
        for elem in lst:
            if elem == element:
                num_element += 1

        assert returned_count == num_element


# =============================================================================


def test_list_sort():
    """
    Test list.sort(reverse):
        - reverse = True: sorted in Descending order
        - reverse = False: sorted in Ascending order
    """
    num_test = 10

    for _ in range(num_test):
        lst, len_list = create_random_list()

        reverse = random.choice([True, False])
        lst.sort(reverse=reverse)

        test_val = True
        for i in range(len_list - 1):
            if reverse and lst[i] < lst[i + 1]:
                test_val = False
                break
            elif not reverse and lst[i] > lst[i + 1]:
                test_val = False
                break

        assert test_val


# =============================================================================


def test_list_copy():
    """
    Test list.copy():
        - new_list == old_list
        - New list is not old list
    """
    num_test = 10

    for _ in range(num_test):
        lst, _ = create_random_list()

        new_lst = lst.copy()

        assert new_lst == lst
        assert new_lst is not lst


# =============================================================================


def test_list_all():
    """
    Test function all(list):
        - (any elements in list = False) == False
        - (all elements in list = True) == True
    """
    num_test = 10

    for _ in range(num_test):
        lst, _ = create_random_list()

        returned_val = all(lst)

        test_val = True
        for elem in lst:
            test_val = bool(elem)
            if not test_val:
                break

        assert test_val == returned_val


# =============================================================================


def test_list_any():
    """
    Test function any(list):
        - (any elements in list = True) == True
    """
    num_test = 10

    for _ in range(num_test):
        lst, _ = create_random_list()

        returned_val = any(lst)

        test_val = False
        for elem in lst:
            test_val = bool(elem)
            if test_val:
                break

        assert test_val == returned_val


# =============================================================================


def test_list_enumerate():
    """
    Test function enumerate(list):
        - [(0, value_0), (1, value_1), (2, value_2), ...]
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        lst, len_list = create_random_list()

        val_start = random.randint(lower, upper)
        enumerate_lst = list(enumerate(lst, start=val_start))

        test_val = True
        for i in range(len_list):
            if enumerate_lst[i][1] != lst[enumerate_lst[i][0] - val_start]:
                test_val = False
                break

        assert test_val


# =============================================================================


def test_list_len():
    """
    Test function len(list):
        - Return length of list
    """
    num_test = 10

    for _ in range(num_test):
        lst, len_list = create_random_list()

        assert len_list == len(lst)


# =============================================================================


def test_list_max():
    """
    Test function max(list):
        - Return the maximum value of element in list
    """
    num_test = 10

    for _ in range(num_test):
        lst, len_list = create_random_list()

        max_element = max(lst)

        max_test = lst[0]
        for i in range(len_list):
            if max_test < lst[i]:
                max_test = lst[i]

        assert max_element == max_test


# =============================================================================


def test_list_min():
    """
    Test function min(list):
        - Return the minimum value of element in list
    """
    num_test = 10

    for _ in range(num_test):
        lst, len_list = create_random_list()

        min_element = min(lst)

        min_test = lst[0]
        for i in range(len_list):
            if min_test > lst[i]:
                min_test = lst[i]

        assert min_element == min_test


# =============================================================================


def test_list_sum():
    """
    Test function sum(list, value):
        - list[0] + list[1] + ... + list[-1] + value == sum(list, value)
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        lst, _ = create_random_list()

        val_start = random.randint(lower, upper)
        sum_of_lst = sum(lst, start=val_start)

        sum_test = val_start
        for elem in lst:
            sum_test += elem

        assert sum_test == sum_of_lst


# =============================================================================


def test_list_reverse():
    """
    Test function reverse(list):
        - new_list == old_list[::-1]
    """
    num_test = 10

    for _ in range(num_test):
        old_lst, _ = create_random_list()
        new_lst = old_lst[:]

        new_lst.reverse()

        assert new_lst == old_lst[::-1]


# =============================================================================
