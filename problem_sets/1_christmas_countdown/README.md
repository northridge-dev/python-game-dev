# Christmas Countdown

Write a program that prompts the user for a date (day, month and year)
and displays the number of days until Christmas.

## How to submit

Show me your program. We'll run it a few times, execute the tests,
and I'll ask you some questions about your code.

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

- Do NOT use the `datetime` module (at least not until you get to Bonus #2).

## Bonus

1. Account for leap years. (To do so, you'll also need to ask the user for the current
   year.)

2. Write a second version of your program that makes use of Python's `datetime` module.

   - Now that you have access to the `datetime` module, use the current date
     as a default input value so a user can get the number of days from now
     until Christmas without inputting the date, but could still provide a
     different date if desired.

3. Expand your program to handle other holidays.
