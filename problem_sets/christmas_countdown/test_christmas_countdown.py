import pytest
from christmas_countdown import get_days_until_christmas

"""
These are the tests that will be run to check your work. You can
add a test if you'd like, but don't change the existing tests.
"""


def test_christmas_countdown():
    assert get_days_until_christmas(12, 25, 2024) == 0
    assert get_days_until_christmas(12, 24, 2024) == 1

    # handle a day after Christmas
    assert get_days_until_christmas(12, 27, 2024) == 363

    # handle a day after leap day
    assert get_days_until_christmas(11, 11, 2024) == 44


# Uncomment the line below after completing the first bonus challenge
# @pytest.mark.skip(reason="include test only BEFORE finishing bonus challenge #1")
def test_christmas_countdown_unhandled_leap_year():
    # handle a day after Christmas when following year is a leap year
    assert get_days_until_christmas(12, 27, 2023, False) == 363
    # handle a day before leap day
    assert get_days_until_christmas(2, 25, 2024, False) == 303
    assert get_days_until_christmas(2, 25, 2025, False) == 303


# Comment out the line below after completing the first bonus challenge
@pytest.mark.skip(reason="include test only AFTER finishing bonus challenge #1")
def test_christmas_countdown_leap_year():
    # handle a day after Christmas when following year is a leap year
    assert get_days_until_christmas(12, 27, 2023, True) == 364
    # handle a day before leap day
    assert get_days_until_christmas(2, 25, 2024, True) == 304
    assert get_days_until_christmas(2, 25, 2025, True) == 303
