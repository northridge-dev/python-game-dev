"""
Fun fun functions!

Functions are blocks of code that can be called (or executed or invoked) from
anywhere in the program. Functions help you avoid repeating code over and over.
They also can help you simplify code by abstracting away the details of how
some functionality is implemented.
"""

"""
 To define a function, you need:
 - the `def` keyword
 - the name of the function (try to make it descriptive!)
 - parentheses (these can be empty or contain parameters)
 - a colon
 - the body of the function (indented)
 - a return statement (optional)
"""

"""
Basics
"""


# We've alredy seen a very simple function:
def hello_world():
    print("Hello, world!")


# This function doesn't take any arguments (or parameters) and doesn't return a value.
# Instead, it has a "side-effect" of printing "Hello, world!" to the console.

# Call (or execute or invoke) the function by using its name and parentheses.
hello_world()  # Hello, world!


# Here's what it looks like when a function takes arguments (or parameters)
# and returns a value:
def add_two(base_number):
    return base_number + 2


# Here's what it looks like to call a function with an argument:
add_two(5)

# If you this function definition in a Python interpretor and call it with an
# argument, you'll see the return value printed to the console. It looks like
# it's printing the value in the same way that our hello_world() function did,
# but it's actually returning the value and the interpretor is printing it for
# us.
add_two(3)  # 5

# We can see the differed between printing and returning if we try to save the
# return value to a variable:
sum = add_two(3)
greeting = hello_world()
print("sum: ", sum)
print("greeting: ", greeting)

# From this experiment, we can conclude that, if we don't explicitly return a
# value from a function, the function implicitly returns `None`.


# A function can take any number of arguments.
def add_func(num1, num2):
    return num1 + num2


# Here's what it looks like to call a function with multiple arguments:
print("add_func(3, 4): ", add_func(3, 4))  # 7


"""
Function scope
"""
# Pause and think about what's happening with the arguments we're passing to `add_func`:
#  - calling `add_func` tells Python: look up the code block saved as `add_func` and execute it
#  - Assign the first argument I provided to the parameter `num1`. That's just a variable assignment!
#  - Assign the second argument I provided to the parameter `num2`. That's just another variable assignment!
#  - Perform the calculation I defined in the function body and return to me the result

# `num1` and `num2` have a meaning within the `add_func` function, but outside the function,
# they don't have a meaning. We can't access them outside the function.
# print('num1: ', num1)  #! NameError: name 'num1' is not defined
# print('num2: ', num2)  #! NameError: name 'num2' is not defined


# This is called "scope". The variables `num1` and `num2` are defined within the scope of the
# function, but not outside the it.
#
# Each function has its own scope. We can define variables with the same name in different functions
# without any problems. They are completely separate variables.
def subtract_func(num1, num2):
    return num1 - num2


print("add_func(3, 4): ", add_func(3, 4))  # 7
print("subtract_func(3, 4): ", subtract_func(3, 4))  # -1


# Scope applies not only to parameters, but also to variables defined within the function body.
def just_return_one():
    function_scoped_variable = "you can't access me outside of just_return_one!"
    print(
        "function_scoped_variable inside of just_return_one: ", function_scoped_variable
    )
    return 1


print("just_return_one(): ", just_return_one())  # 1
# print("function_scoped_variable outside of just_return_one: ", function_scoped_variable)  #! NameError: name 'functin_scoped_variable' is not defined

# While we can't access variables defined within a function outside of that function, we can access
# variables defined in an "outer scope".

# The outermost scope is called the "global scope". Variables defined in the global scope are accessible
# from anywhere in the program.
global_variable = "Anyone can access me!"


def print_global_variable():
    print("global_variable inside of print_global_variable: ", global_variable)


print("global_variable outside of print_global_variable: ", global_variable)
print_global_variable()


# When Python looks up the value of a variable, it will first look in the current scope. If it doesn't
# find the variable there, it will look in the next outer scope. It will continue to look in outer scopes
# until it finds the variable or it reaches the global scope. If it doesn't find the variable in the global
# scope, it will raise an error.
def outer_function():
    outer_scope_variable = "I'm in the outer scope!"

    def inner_function():
        inner_scope_variable = "I'm in the inner scope!"
        print("inner_scope_variable inside of inner_function: ", inner_scope_variable)
        print("outer_scope_variable inside of inner_function: ", outer_scope_variable)
        print("global_variable inside of inner_function: ", global_variable)

    inner_function()


outer_function()

# (Yes, you can define a function *within* another function)


"""
A bit more about functions
"""

# So far, we've called functions using *positional* arguments -- the order of the arguments matters.
# But you can also call a function using *keyword* arguments -- the order doesn't matter because we
# specify which argument is which.
def greet(first, last):
    return f"Hello, {first} {last}!" # f-strings are a convenient way to insert variables into a string

# These three function calls will have the same return value:
greet("Nico", "Hoerner")
greet(first="Nico", last="Hoerner")
greet(last="Hoerner", first="Nico")

# We saw earlier that a function can take any number of arguments.
# Fun fact: a function can even take an indefinite number of arguments.
# Sidenote: we've been using the built-in `print` function, which is a
# real-life example of a function that can take an indefinite number of arguments.
def how_many_args(*args):
    return len(args)


how_many_args(1, 2, 3, 4, 5)  # 5


# Instead of a value, you can also pass a variable as an argument to a function.
variable_to_use_as_an_argument = 5
add_func(variable_to_use_as_an_argument, 3)  # 8

# You can pass as an argument an expression that evaluates to a value
add_func(4 + 2, 3)  # 9
subtract_func(
    variable_to_use_as_an_argument * 2, variable_to_use_as_an_argument / 2
)  # 7.5

# You can pass as an argument the return value of another function
add_func(add_two(3), 3)  # 8
subtract_func(add_func(5, 6), subtract_func(6, 5))  # 10
subtract_func(add_func(5, 6), subtract_func(add_func(3, subtract_func(6, 3)), 5))  # ??


# You've seen that one function can call another.
# Ready to have your mind blow? A function can also call itself!
def recursive_add(first, second):
    if second == 0:
        return first

    return recursive_add(first + 1, second - 1)


recursive_add(5, 3)  # 8
