"""
Function create two vectors
"""

import numpy as np
import random

# =============================================================================


def create_two_vectors():
    """
    Function create two vectors with a number of plans
    :return: vector_a, vector_b
    """
    lower, upper = 0, 1000
    num_plan = random.randint(1, 1000)

    vector_a = np.array([random.randint(lower, upper) for _ in range(num_plan)])
    vector_b = np.array([random.randint(lower, upper) for _ in range(num_plan)])

    return vector_a, vector_b
