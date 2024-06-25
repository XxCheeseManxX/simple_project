"""Testing with Numpy.

For learning purposes
"""

import numpy as np


def numpy_mean(array: list) -> list:
    """Return the mean of the array parameter."""
    array = np.array(array)
    return np.mean(array)
