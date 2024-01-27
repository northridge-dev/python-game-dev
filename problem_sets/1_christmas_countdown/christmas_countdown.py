"""
Here's where you'll write your code. 
  - Follow the instructions in the README file.
  - You'll need to write get_days_until_christmas 
  - You may also need to modify christmas_countdown, but be careful!

For bonus challenges: 
  - Except for #3, add bonus challenge code to get_days_until_christmas
    and christmas_countdown.
  - For #3, write get_days_until_christmas_datetime and call it (instead
    of get_days_until_christmas) from christmas_countdown.

Run your code from the terminal:
  - make sure you're in the right directory (1_christmas_countdown)
    - if you're not sure how to get to the right directory, ask!
  - make sure you're at the command line prompt, not in the Python shell
  - type the following command: python christmas_countdown.py

To run the tests:
  - make sure you're in the right directory (1_christmas_countdown)
  - make sure you're at the command line prompt, not in the Python shell
  - type the following command: pytest
"""

""" Write this function only when you get to bonus challenge #3 """


def get_days_until_christmas_datetime(month, day, year):
    pass  # Delete this line and write your code here instead


def get_days_until_christmas(month, day):
    pass  # Delete this line and write your code here instead


def christmas_countdown():
    month = int(input("What month is it? (1-12) "))
    day = int(input("What day is it? (1-31) "))

    days_until_christmas = get_days_until_christmas(month, day)

    if days_until_christmas == 0:
        print("Merry Christmas!")
    elif days_until_christmas == 1:
        print("Merry Christmas Eve!")
    else:
        print(f"Only {days_until_christmas} days 'til Christmas!")


"""
These are the tests that will be run to check your work. You can
add a test if you'd like, but don't change the existing tests.
"""


# These tests are for the base assignment only.
# Once you start working on the bonus challenges, comment these out
# and instead use the appropriate bonus tests, below.
def test_base_assignment():
    assert get_days_until_christmas(12, 25) == 0
    assert get_days_until_christmas(12, 24) == 1

    # handle a day after Christmas
    assert get_days_until_christmas(12, 27) == 363

    # handle a day after leap day
    assert get_days_until_christmas(11, 11) == 44

    # handle a day before leap day
    assert get_days_until_christmas(2, 25) == 303


"""
Don't worry about the code, below, and don't change it.

It's just a way to trigger the christmas_countdown function
when you run this file from the command line.
"""
if __name__ == "__main__":
    christmas_countdown()
