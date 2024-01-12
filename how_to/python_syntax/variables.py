import math

"""
Variables store data in memory.
"""

# To create a variable, we use the assignment operator (=)
my_variable = 10
print("The value of 'my_variable' is ", my_variable)

# Varaiables can be reassigned
my_variable = 20
print("The value of 'my_variable' is ", my_variable)

# Variables can be of any type. Here are some examples of simple types.
integer_variable = 99
float_variable = 99.99
boolean_variable = True
string_variable = "Hello World"

# You can assign the result of a calculation to a variable
sum = 5 + 6
gcd = math.gcd(36, 24)  # library functions have to be imported; see top of the file

# Sometimes operators are "overloaded" -- what they do
# depends on the type of values they operate on
concatenated_string = "Hello" + " " + "World!"

# You can one variable to set another variable
# Python will evaluate the righthand side of the assignment operator first,
# subbing in 5 for a_number and 6 for another_number
a_number = 5
another_number = 6
another_sum = a_number + another_number

# If can use a variable on the righthand side of
# the assignment operator even if you're reassigning the same variable
count = 5
count = count + 2
count = count - 3

# But there's a more concise and "Pythonic" way to do it
pythonic_count = 5
pythonic_count += 2
pythonic_count -= 3

# We can even assign multiple variables at once
first, second = 1, 2
print("first: ", first)
print("second: ", second)
