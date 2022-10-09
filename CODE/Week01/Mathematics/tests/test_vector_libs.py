"""
Testing operators of vector
"""

import random
import math
import numpy as np
from libs import operators_vector
from libs.create_vector import create_two_vectors

# =============================================================================


def test_add_vector():
    """
    Test function add_vectors(vector_a, vector_b)
        - add_vectors(vector_a, vector_b) == vector_a[:] + vector_b[:]
    """
    num_test = 10

    for _ in range(num_test):
        vector_a, vector_b = create_two_vectors()

        add_vector = operators_vector.add_vectors(vector_a, vector_b)

        assert all(np.equal(add_vector, vector_a[:] + vector_b[:]))


# =============================================================================


def test_sub_vector():
    """
    Test function add_vectors(vector_a, vector_b):
        - add_vectors(vector_a, vector_b) == vector_a[:] - vector_b[:]
    """
    num_test = 10

    for _ in range(num_test):
        vector_a, vector_b = create_two_vectors()

        sub_vector = operators_vector.sub_vectors(vector_a, vector_b)

        assert all(np.equal(sub_vector, vector_a[:] - vector_b[:]))


# =============================================================================


def test_mul_vec_scal():
    """
    Test function multi_vector_scalar(vector, scalar):
        - multi_vector_scalar(vector, scalar) == vector[:] * scalar
    """
    num_test = 10
    lower, upper = 0, 1000

    for _ in range(num_test):
        vector, _ = create_two_vectors()
        scal = random.randint(lower, upper)

        result = operators_vector.multi_vector_scalar(vector, scal)

        assert all(np.equal(result, vector[:] * scal))


# =============================================================================


def test_mag_vec():
    """
    Test function magnitude_vector(vector):
        - mag_vec == sqrt(vector[0]^2 + vector[1]^2 + ... vector[-1]^2)
    """
    num_test = 10

    for _ in range(num_test):
        vector, _ = create_two_vectors()

        returned_val = operators_vector.magnitude_vector(vector)

        mag_square_vec = 0
        for elem in vector:
            mag_square_vec += elem**2

        assert math.sqrt(mag_square_vec) == returned_val


# =============================================================================


# TO EDIT
def test_dir_vec():
    """
    Test function direction_vector(vector):
        - dir_vector == [vector[0] / mag_vector, vector[1] / mag_vector, ...]
    """
    num_test = 10

    for _ in range(num_test):
        vector, _ = create_two_vectors()

        dir_vec = operators_vector.direction_vector(vector)
        mag_vec = operators_vector.magnitude_vector(vector)

        assert all(np.equal(dir_vec, vector[:] / mag_vec))


# =============================================================================


def test_scal_prod():
    """
    Test function scalar_product(vector_a, vector_b):
        - sum(vector_a * vector_b) = vector_a.dot(vector(b)
    """
    num_test = 10

    for _ in range(num_test):
        vector_a, vector_b = create_two_vectors()

        returned_val = operators_vector.scalar_product(vector_a, vector_b)

        test_val = sum(vector_a * vector_b)

        assert returned_val == test_val


# =============================================================================
