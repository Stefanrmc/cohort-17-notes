import pytest

from latest_time import (get_first_digit,
                         get_second_digit,
                         get_third_digit)


def test_get_first_digit_returns_zero():
    assert get_first_digit([0, 9, 3, 8]) == 0


def test_get_first_digit_returns_one():
    assert get_first_digit([1, 9, 8, 3]) == 1


def test_get_first_digit_returns_two():
    assert get_first_digit([9, 1, 2, 5]) == 2


def test_get_second_digit_with_first_digit_two():
    assert get_second_digit([2, 5, 9], 2) == 2


def test_get_second_digit_with_first_digit_as_two_and_multiple_valid_digits():
    assert get_second_digit([1, 0, 9], 2) == 1


@pytest.mark.parametrize(["first", "second", "third", "fourth"],
                         ())
