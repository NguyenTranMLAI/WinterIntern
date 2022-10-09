"""
Testing cases of method and function of DICTIONARY
"""

import random
from libs.create_dict import create_random_dict
from libs.create_set import create_random_set

# =============================================================================


def test_dict_clear():
    """
    Test dict_clear():
        - dict == {}
    """
    num_test = 10

    for _ in range(num_test):
        sample_dict = create_random_dict()

        sample_dict.clear()

        assert len(sample_dict) == 0


# =============================================================================


def test_dict_copy():
    """
    Test dict.copy():
        - dict_copy == dict.copy()
        - dict_copy is not dict
    """
    num_test = 10

    for _ in range(num_test):
        sample_dict = create_random_dict()

        dict_copy = sample_dict.copy()

        assert sample_dict == dict_copy
        assert sample_dict is not dict_copy


# =============================================================================


def test_dict_fromkeys():
    """
    Test dict.fromkeys(key, value):
        - new_dict == {key_0: value, key_1: value, ...}
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        keys_dict = create_random_set()
        value = random.randint(lower, upper)

        sample_dict = dict.fromkeys(keys_dict, value)

        test_val = True
        for k in sample_dict:
            if sample_dict[k] != value:
                test_val = False
                break

        assert len(sample_dict) == len(keys_dict)
        assert test_val


# =============================================================================


def test_dict_get():
    """
    Test dict.get(key, value):
        - key in dict: dict.get(key, value) == dict[key]
        - key not in dict: dict.get(key, value) == value
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        sample_dict = create_random_dict()

        key = random.randint(lower, upper)
        value = random.randint(lower, upper)

        if key in sample_dict:
            assert sample_dict.get(key, value) == sample_dict[key]
        else:
            assert value == sample_dict.get(key, value)


# =============================================================================


def test_dict_items():
    """
    Test dict.items():
        - dict_items([(key_0, value_0), (key_1, value_1), ...]) == dict.items()
    """
    num_test = 10

    for _ in range(num_test):
        sample_dict = create_random_dict()

        list_elements = list(sample_dict.items())

        test_val = True
        idx = 0
        for k in sample_dict:
            if k != list_elements[idx][0] or sample_dict[k] != list_elements[idx][1]:
                test_val = False
                break
            idx += 1

        assert len(list_elements) == len(sample_dict)
        assert test_val


# =============================================================================


def test_dict_keys():
    """
    Test dict.keys():
        - list(dict.keys()) == list(dict)
    """
    num_test = 10

    for _ in range(num_test):
        sample_dict = create_random_dict()

        assert list(sample_dict.keys()) == list(sample_dict)


# =============================================================================


def test_dict_pop():
    """
    Test dict.pop(key):
        - old_dict[key] == dict.pop(key)
        - key not in new_dict
        - new_len == old_len - 1
    """
    num_test = 10

    for _ in range(num_test):
        sample_dict = create_random_dict()
        old_len = len(sample_dict)

        key = random.choice(list(sample_dict))
        value_test = sample_dict[key]

        value_returned = sample_dict.pop(key)

        assert len(sample_dict) == old_len - 1
        assert key not in sample_dict
        assert value_returned == value_test


# =============================================================================


def test_dict_popitem():
    """
    Test dict.popitem():
        - new_len = old_len - 1
        - key_end not in new dict
        - (key_end, value_end) of old dict == dict.popitem()
    """
    num_test = 10

    for _ in range(num_test):
        sample_dict = create_random_dict()
        old_len = len(sample_dict)

        end_key = list(sample_dict)[-1]
        end_value = sample_dict[end_key]

        returned_element = sample_dict.popitem()

        assert len(sample_dict) == old_len - 1
        assert end_key == returned_element[0] and end_value == returned_element[1]
        assert end_key not in sample_dict


# =============================================================================


def test_dict_setdefault():
    """
    Test dict.setdefault(key, value):
        - key in dict: dict[value] == dict.setdefault(key, value)
        - key not in dict: value == dict.setdefault(key, value)
                           key in new dict
                           new_len == old_len + 1
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        sample_dict = create_random_dict()
        old_len = len(sample_dict)

        key = random.randint(lower, upper)
        if key in sample_dict:
            assert sample_dict[key] == sample_dict.setdefault(key)
        else:
            value_returned = sample_dict.setdefault(key, random.randint(lower, upper))

            assert key in sample_dict
            assert len(sample_dict) == old_len + 1
            assert sample_dict[key] == value_returned


# =============================================================================


def test_dict_update():
    """
    Test dict_1.update(dict_2):
        - {keys: values of keys} of dict_2 in dict_1
    """
    num_test = 10

    for _ in range(num_test):
        sample_dict_1 = create_random_dict()
        sample_dict_2 = create_random_dict()

        sample_dict_1.update(sample_dict_2)

        test_val = True
        for k in sample_dict_2:
            if k not in sample_dict_1 or sample_dict_2[k] != sample_dict_1[k]:
                test_val = False
                break

        assert test_val


# =============================================================================


def test_dict_values():
    """
    Test dict.values():
        - dict_values([value_0, value_1, ...]) == dict.values()
    """
    num_test = 10

    for _ in range(num_test):
        sample_dict = create_random_dict()

        list_values = list(sample_dict.values())

        test_val = True
        idx = 0
        for k in sample_dict:
            if sample_dict[k] != list_values[idx]:
                test_val = False
                break
            idx += 1

        assert len(list_values) == len(sample_dict)
        assert test_val
