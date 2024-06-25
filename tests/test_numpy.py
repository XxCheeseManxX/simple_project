# ruff: noqa

from src import array


def test_numpy_mean():
    assert array.numpy_mean([1, 2, 3]) == 2
