import pytest
from hello import add


def test_add_positive_numbers():
    assert add(2, 2) == 4


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_positive_and_negative():
    assert add(1, -1) == 0


def test_add_zero():
    assert add(0, 0) == 0


def test_add_large_numbers():
    assert add(1000000, 1000000) == 2000000
