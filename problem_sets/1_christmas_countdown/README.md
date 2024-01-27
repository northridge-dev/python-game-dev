# Christmas Countdown

Write a program that prompts the user for a date (day and month)
and displays the number of days until Christmas.

## Clarifications

- Days-until counting can be ambiguous. Here's what you're aiming for:
  - if today is December 24th, then Christmas is 1 day away
  - if today is December 25th, then Christmas is 0 days away
  - if today is December 26th, then Christmas is 364 days away
    (supposing next year is not a leap year)

## Things to consider

- How will you handle the case where the input date is past Christmas?
- What will your program do if someone enters an invalid date?

## Constraints

- Do NOT use the `datetime` module (at least not until you get to Bonus #3).

## Bonus

1. Use the current date as a default value so a user can get the number of days from
   now until Christmas without typing out the date, but could still provide a different
   date if desired.
2. Account for leap years. (To do so, you'll also need to ask the user for the current
   year.)
3. Write a second version of your program that makes use of Python's `datetime` module.
4. Expand your program to handle other holidays.
