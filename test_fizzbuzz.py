"""Perform tests of the fizz_buzz function."""
import pytest

from fizzbuzz import fizzbuzz

inputs = [3, 5, 15, 4, 10, 115, 7]
outputs = ["fizz", "buzz", "fizzbuzz", "4", "buzz", "buzz", "7"]


@pytest.mark.parametrize("inp,out", zip(inputs, outputs))
def test_fizzbuzz(inp, out):
    """Takes inputs, gets the output of the fizz_buzz function.
    Asserts whether equality holds.
    """
    assert fizzbuzz(inp) == out
