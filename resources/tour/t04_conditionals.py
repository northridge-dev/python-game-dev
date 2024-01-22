"""
Python conditionals: if, elif, else
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
