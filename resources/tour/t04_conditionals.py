"""
Python conditionals: if, else, elif 
"""
# Often, you'll want to execute a block of code only if a certain condition is met.
# That's what conditionals are for.

# The simplest conditional is the `if` statement.
# If the expression after the `if` keyword evaluates to `True`, the indented
# block of code below it will be executed.
# If the expression evaluates to `False`, the block will be skipped.
if 1 + 1 == 2:
    print("Math works!")

# Here's a more concrete example. Imagine you only want to decrement the variable
# keeping track of remaining guesses if the current guess is wrong.
secret_word = "python"
current_guess = "a"
remaining_guesses = 5

if current_guess not in secret_word:
    remaining_guesses -= 1

# In the examples above, if the condition is not met, the code within the "if" block
# is skipped. But what if you want to execute a different block of code if the condition
# is not met? That's what `else` is for.
if 1 + 1 == 3:
    print("Math is broken")
else:
    print("Math may not be broken, but we can't be sure")

# Here's the pattern:
# if <condition>:
#    <code to execute if <condition> is met>
# else:
#   <code to execute if <condition> is not met>

# Let's extend the example we used above:
current_guess = "o"
if current_guess not in secret_word:
    remaining_guesses -= 1
else:
    print("Yes! The secret word contains the letter: ", current_guess)

# Of course we could have changed the order of the if and else blocks as long as
# we also change the condition. Sometimes it's equally clear and a matter of preference.
# Other times, the logic of your program will make one approach simpler.
if current_guess in secret_word:
    print("Yes! The secret word contains the letter: ", current_guess)
else:
    remaining_guesses -= 1

# Sometimes you'll want to check multiple conditions. That's what `elif` is for.
# Here's the pattern:
# if <condition1>:
#     <code to execute if <condition1> is met>
# elif <condition2>:
#     <code to execute if <condition2> is met>
# elif <condition3>:
#     <code to execute if <condition3> is met>
# else:
#     <code to execute if none of the earlier conditions are met>

# For example, you might you a sting of 'elif' statements to convert a numeric
# score into a letter grade.
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

# Notice that several of those conditions are true: score >= 80, score >= 70, & score >= 60,
# but only the first code block where the condition was met was executed.

# Conditionals can also be nested.
# Here's a BAD example:
score = 85

if score >= 90:
    grade = "A"
else:
    if score >= 80:
        grade = "B"
    else:
        if score >= 70:
            grade = "C"
        else:
            if score >= 60:
                grade = "D"
            else:
                grade = "F"

# It will do the same thing as our 'elif' example, but it's much harder to read and understand.
# (By the way, Google Bard -- an LLM-powered chat agent -- gave me this bit of bad code. But
# when I asked Bard if using 'elif' conditionals would be better, it readily agreed.)

# Here's a better example:
# A year is a leap year if it is evenly divisible by 4 except years that are divisible by 100 but
# not divisble by 400.


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    return is_leap_year


# This works, but it is also hard to understand. Very often, if you find yourself with deeply
# nested conditionals, you can find a simpler way to think about the problem.


def leap_year_simpler(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return year % 400 == 0
    else:
        return True


# Because returning a value ends the function's execution, the 'else' isn't necessary. This is equivalent:
def leap_year_simpler_alt(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return year % 400 == 0

    return True


# Or maybe we don't need conditionals at all, just Boolean operators . . .


def leap_year_simplest(year):
    return year % 4 == 0 and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0))
