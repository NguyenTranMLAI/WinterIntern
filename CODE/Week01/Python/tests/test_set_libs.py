"""
Testing cases of method and function of SET
"""

import random
from libs.create_set import create_random_set

# =============================================================================


def test_set_discard():
    """
    Test set.discard(val):
        - val in set: new_len == old_len - 1
                      val not in set
        - val not in set: new_len == old_len
    """
    num_tests = 10
    lower, upper = 0, 1000

    for _ in range(num_tests):
        sample_set = create_random_set()
        old_len = len(sample_set)

        num_remove = random.randint(lower, upper)
        sample_set.discard(num_remove)

        if num_remove in sample_set:
            assert num_remove not in sample_set
            assert len(sample_set) == old_len - 1
        else:
            assert len(sample_set) == old_len


# =============================================================================


def test_set_intersection():
    """
    Test set_1.intersection(set_2):
        - all elements of set_3 in set_1 and in set_2
    """
    num_tests = 10

    for _ in range(num_tests):
        sample_set_1 = create_random_set()
        sample_set_2 = create_random_set()

        intersection_elements = sample_set_1.intersection(sample_set_2)

        test_val = True
        for i in intersection_elements:
            if i not in sample_set_1 or i not in sample_set_2:
                test_val = False
                break

        assert test_val


# =============================================================================


def test_set_isdisjoint():
    """
    Test set_1.isdisjoint(set_2):
        - any elements of set not in other set
    """
    num_tests = 10

    for _ in range(num_tests):
        sample_set_1 = create_random_set()
        sample_set_2 = create_random_set()

        assert sample_set_1.isdisjoint(sample_set_2) == (
            len(sample_set_1.intersection(sample_set_2)) == 0
        )


# =============================================================================


def test_set_union():
    """
    Test set_1.union(set_2)
        - len(union_elements) == len(set_1) + len(set_2) - len(set_1.intersection(set_2))
        - any union elements in set_1 or in set_2
    """
    num_tests = 10

    for _ in range(num_tests):
        sample_set_1 = create_random_set()
        sample_set_2 = create_random_set()

        union_elements = sample_set_1.union(sample_set_2)

        test_val = True
        for elem in union_elements:
            if elem not in sample_set_1 and elem not in sample_set_2:
                test_val = False
                break

        assert len(union_elements) == len(sample_set_1) + len(sample_set_2) - len(
            sample_set_1.intersection(sample_set_2)
        )
        assert test_val


# =============================================================================


def test_set_difference():
    """
    Test set_1.difference(set_2):
        - difference_elements == set_1 - set_1.intersection(set_2)
        - elements of set_1 not in set_2
    """
    num_tests = 10

    for _ in range(num_tests):
        sample_set_1 = create_random_set()
        sample_set_2 = create_random_set()

        difference_elements = sample_set_1.difference(sample_set_2)

        assert difference_elements == sample_set_1 - sample_set_1.intersection(
            sample_set_2
        )


# =============================================================================


def test_set_symmetric_difference():
    """
    Test set_1.symmetric_difference(set_2):
        - set_1.symmetric_difference(set_2) == set_1.union(set_2) - set_1.intersection(set_2)
        - elements of set_1 not in set_2 and of set_2 not in set_1
    """
    num_tests = 10

    for _ in range(num_tests):
        sample_set_1 = create_random_set()
        sample_set_2 = create_random_set()

        assert sample_set_1.symmetric_difference(sample_set_2) == sample_set_1.union(
            sample_set_2
        ) - sample_set_1.intersection(sample_set_2)


# =============================================================================
