"""
Create add function for vectors
"""

import math
import numpy as np

# =============================================================================


def add_vectors(vector_a, vector_b):
    """
    Add of vector a and vector b
    :param vector_a: [aj, ai]
    :param vector_b: [aj, ai]
    :return: [aj + bj, ai + bi]
    """
    return vector_a + vector_b


# =============================================================================


def sub_vectors(vector_a, vector_b):
    """
    Subtraction of vector a for vector b
    :param vector_a: [aj, ai]
    :param vector_b: [aj, ai]
    :return: [aj - bj, ai - bi]
    """
    return vector_a - vector_b


# =============================================================================


def multi_vector_scalar(vector, scalar):
    """
    The multiplication of a vector by a scalar
    :param vector: [j, i]
    :param scalar: a
    :return: [a*j, a*i]
    """
    return vector * scalar


# =============================================================================


def magnitude_vector(vector):
    """
    The magnitude of vector is a distance from the endpoint to the origin
    :param vector: [j ,i]
    :return: sqrt(j^2 - i^2)
    """
    return np.linalg.norm(vector)


# =============================================================================


def direction_vector(vector):
    """
    Vector = mag(vector) * dir(vector)
    => dir(vector) = vector / mag(vector)
    :param vector: [j, i]
    :return: [j / ||vector||, i / ||vector||]
    """
    magnitude = magnitude_vector(vector)

    return multi_vector_scalar(vector, 1 / magnitude)


# =============================================================================


def scalar_product(vector_a, vector_b):
    """
    A scalar product (a dot product): vector_a . vector_b
    :param vector_a: [aj, ai]
    :param vector_b: [bj, bi]
    :return: aj*bj + ai*bi
    """
    return vector_a.dot(vector_b)


# =============================================================================


def angle_between_vectors(vector_a, vector_b):
    """
    vector_a . vector_b = mag(vector_a) * mag(vector_b) * cos(alppha)
    alpha = arccos{(vector_a * vector_b) / [mag(vector_a) * mag(vector_b)]}
    :param vector_a: [aj, ai]
    :param vector_b: [bj, bi]
    :return: angle between vectors (radian unit)
    """
    a_dot_b = scalar_product(vector_a, vector_b)
    mag_a = magnitude_vector(vector_a)
    mag_b = magnitude_vector(vector_b)

    return math.acos(a_dot_b / (mag_a * mag_b))


# =============================================================================


def scalar_project(vector_a, vector_b):
    """
    The scalar projection of vector_a on vector_b is a scalar equal to
    scalar_project_a = mag(vector_a) * cos(angle of vector_a and vector_b)
       = vector_a . vector_b / mag(vector_b)
    :param vector_a: [aj, ai]
    :param vector_b: [bj, bi]
    :return: vector_a . vector_b / mag(vector_b)
    """
    a_dot_b = scalar_product(vector_a, vector_b)
    mag_b = magnitude_vector(vector_b)

    return a_dot_b / mag_b


# =============================================================================


def vector_project(vector_a, vector_b):
    """
    The vector projection of vector_a on vector_b is a vector
    whose magnitude is the scalar projection of a on b with the same direction as b.
    It is defined as: vector_project_a = scalar_project_a * dir(vector_b)
    :param vector_a: [aj, ai]
    :param vector_b: [bj, bi]
    :return: scalar_project(vector_a, vector_b) * direction_vector(vector_b)
    """
    scalar_proj_a = scalar_product(vector_a, vector_b)
    dir_b = direction_vector(vector_b)

    return scalar_proj_a * dir_b


# =============================================================================
