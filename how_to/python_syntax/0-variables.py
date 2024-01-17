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
print("5 + 6 = ", sum)
gcd = math.gcd(36, 24)  # library functions have to be imported; see top of the file
print("GCD of 36 and 24 is ", gcd)

# Sometimes operators are "overloaded" -- what they do
# depends on the type of values they operate on
concatenated_string = "Hello" + " " + "World!"

# You can use one variable to set another variable
# Python will evaluate the righthand side of the assignment operator first,
# subbing in 5 for a_number and 6 for another_number
a_number = 5
another_number = 6
another_sum = a_number + another_number
print("another_sum: ", another_sum)

# If can use a variable on the righthand side of
# the assignment operator even if you're reassigning the same variable
count = 5
count = count + 2
print("count after adding: ", count)
count = count - 3
print("count after subtracting: ", count)

# But there's a more concise and "Pythonic" way to do it
pythonic_count = 5
pythonic_count += 2
pythonic_count -= 3
print("pythonic_count: ", pythonic_count)

# Not all calculations involve numbers
# Here are some examples of Boolean "calculations"
coding_is_fun = True
coding_is_hard = True
coding_is_easy = not coding_is_hard
print("Coding is easy? ", coding_is_easy)
kruckenberg_is_consistent = (
    coding_is_hard or coding_is_easy and not (coding_is_hard and coding_is_easy)
)
print("Kruckenberg is consistent? ", kruckenberg_is_consistent)

# We can even assign multiple variables at once
first, second, third = 1, 2, "third"
print("first: ", first)
print("second: ", second)
print("third: ", third)

# We can also assign the same value to multiple variables at once
# This is called "chaining"
a = b = c = 42
print("a: ", a)
print("b: ", b)
print("c: ", c)
print("a == b == c: ", a == b == c)

# We'll look at variables with complex data types when
# we learn about lists, tuples, and dictionaries
