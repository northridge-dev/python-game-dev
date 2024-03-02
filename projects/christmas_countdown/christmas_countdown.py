"""
Here's where you'll write your code. 
  - Follow the instructions in the README file.
  - You'll need to implement `get_days_until_christmas` 
  - You may also need to modify `christmas_countdown`, but be careful!

Run your code from the terminal:
  - make sure you're in the right directory (christmas_countdown)
    - if you're not sure how to get to the right directory, ask!
  - make sure you're at the command line prompt, not in the Python shell (not >>>)
  - type the following command: python christmas_countdown.py

To run the tests:
  - make sure you're in the right directory (christmas_countdown)
  - make sure you're at the command line prompt, not in the Python shell (not >>>)
  - type the following command: pytest
"""


def get_days_until_christmas(month, day, year, check_leap_year=True):
    pass  # Delete this line and write your code here instead


def christmas_countdown():
    month = int(input("What month is it? (1-12) "))
    day = int(input("What day is it? (1-31) "))
    year = int(input("What year is it? (4-digit year) "))

    # Change the last argument to True once you've implemented the first bonus challenge
    days_until_christmas = get_days_until_christmas(month, day, year, False)

    if days_until_christmas == 0:
        print("Merry Christmas!")
    elif days_until_christmas == 1:
        print("Merry Christmas Eve!")
    else:
        print(f"Only {days_until_christmas} days 'til Christmas!")


"""
Don't worry about the code below, and don't change it.

It's just a way to trigger the christmas_countdown function
when you run this file from the command line.
"""
if __name__ == "__main__":
    christmas_countdown()
