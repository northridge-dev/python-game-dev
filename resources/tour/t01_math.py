"""
Math!
"""

# Python has two common number types: integers and floats
integer_ex = 5
float_ex = 5.0
another_float_ex = 5.42

# You can convert between them
print(
    "Convert 5.0 to an integer: ", int(5.0), " ", type(int(5.0))
)  # if you're curious, type() returns the type of a variable or value
print(
    "Convert 5 to a float: ", float(5), " ", type(float(5))
)  # if you're curious, a function that can take an indefinite number of arguments is called a "variadic" function

# What do you think will happen here?
print("Convert 5.5 to an integer: ", int(5.5))

# You can also convert numbers to strings and vice versa
print("Convert 5 to a string: ", str(5), " ", type(5), "-->", type(str(5)))
print("Convert '5' to an integer: ", int("5"), " ", type("5"), "-->", type(int("5")))
print(
    "Convert '5.0' to a float: ",
    float("5.0"),
    " ",
    type("5.0"),
    "-->",
    type(float("5.0")),
)

# Addition, subtraction, and multiplication are simple
# (More on division in just a moment . . .)
print("5 + 6 = ", 5 + 6)
print("5.0 + 6 = ", 5.0 + 6)
print("5 - 6 = ", 5 - 6)
print("5.0 - 6 = ", 5.0 - 6)
print("5 * 6 = ", 5 * 6)
print("5.0 * 6 = ", 5.0 * 6)

# You can compare numers. The result is a Boolean (True or False)
print("5 > 6 ? ", 5 > 6)
# You can compare floats and integers
print("6.0 == 6 ? ", 6.0 == 6)
print("6.001 > 6 ? ", 6.001 > 6)
print("6.001 <= 6 ? ", 6.001 <= 6)
# (Sidenote: you can even compare strings.)
# (What do you suppose makes one string less than or greater than another?)
print("'a' < 'b' ? ", "a" < "b")
# (What would you guess will happen if we try to compare a number to a string?)
# print("'a' < 6 ? ", "a" < 6)

# Here's an example of exponentiation within a comparison
print("2^3 == 2 * 2 * 2 ? ", 2**3 == 2 * 2 * 2)

# Division is a little trickier (and Python 2 and Python 3 handle it differently)
print("6 / 5 = ", 6 / 5)  # not surprising that the answer is a floating point number
print(
    "10 / 5 = ", 10 / 5
)  # maybe a little surprising that the answer is a floating point number

# If you want an integer, you can use the floor division operator (//)
print("10 // 5 = ", 10 // 5)
print("6 // 5 = ", 6 // 5)

# There's also a special operator for getting the remainder of a division (modulo)
# It's the percent sign (%)
print("6 % 5 = ", 6 % 5)
print("10 % 5 = ", 10 % 5)

# Getting the remainder can be useful for checking if a number is even or odd
# (And here's a sneek peak at conditional statements, too.)
if 6 % 2 == 0:
    print("6 is even")
else:
    print("6 is odd")

if 5 % 2 == 0:
    print("5 is even")
else:
    print("5 is odd")
