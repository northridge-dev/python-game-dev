"""
Besides the integers, floats, strings, and booleans we've already
seen, Python has a few common data types:
- lists
- tuples
- dictionaries

These are all "complex" data types, meaning they can store multiple
"simple" or "complex" data types.
"""

""" Lists """
# A list is just an ordered collection of data.
# Enclose a list in square brackets, with each item separated by a comma.
from functools import wraps


shopping_list = ["bread", "milk", "eggs", "cheese", "butter"]

# We just saw that lists can contain strings, but they can also contain
# numbers, booleans, and even other lists!
integer_list = [22, 50, 5, 17]
float_list = [3.14, 2.718, 1.618]
mixed_list = [1, "a", 2, "b", 3, "c"]
list_of_lists = [[1, 2, 3], ["a", "b", "c"], [True, False, True]]

# We can access individual items in a list using their index.
# (An index is just a number that tells us where an item is in a list.)
# Remember that Python is zero-indexed, meaning the first item in a list
# has index 0.
shopping_list[0]  # 'bread'
integer_list[2]  # 5
list_of_lists[1]  # ['a', 'b', 'c']
list_of_lists[2][0]  # True

# What do you suppose will happen if we try to access an index that doesn't
# exist?
# shopping_list[5]  #! IndexError: list index out of range

# Since we'll get ourselves in trouble if we try to access an index that
# doesn't exist, we can use the built-in len() function to get the length
# of a list.
len(shopping_list)  # 5
len(integer_list)  # 4
len(list_of_lists)  # 3

# You _could_ combine len() with an index to get the last item in a list...
shopping_list[len(shopping_list) - 1]  # 'butter'
# But there's a btter way.
# We can use negative indices to access items from the end of a list.
shopping_list[-1]  # 'butter'
float_list[-3]  # 3.14

# You can also use negative indices to get a range of items from a list.
# This is called "slicing".
shopping_list[1:3]  # ['milk', 'eggs']

# If you omit the first index, Python will assume you want to start at the
# beginning of the list.
shopping_list[:3]  # ['bread', 'milk', 'eggs']

# And if you omit the second index, Python will assume you want to go to
# the end of the list.
shopping_list[3:]  # ['cheese', 'butter']

# You can even take a slice of every other item in a list.
# The third number is called the "step".
shopping_list[::2]  # ['bread', 'eggs', 'butter']

# Lists can be modified.
# You can assign a new value to an item in a list using its index.
shopping_list[0] = "bagels"

# For example, you can add items to a list using the `append` method
shopping_list.append("apples")
shopping_list[-1]  # 'apples'

# You can also remove items from a list using the `pop` method.
# If you don't pass an index to `pop`, it will remove the last item in the list.
shopping_list.pop()  # 'apples'
shopping_list  # ['bagels', 'milk', 'eggs', 'cheese', 'butter']

# You can also pass an index to `pop` to remove a specific item.
shopping_list.pop(2)  # 'eggs'

# You can also use the `remove` method to remove a specific item.
# `remove` will remove the first item in the list that matches the value
# you pass to it.
shoppin_list.remove("milk")
shopping_list  # ['bagels', 'cheese', 'butter']

# You can reverse the order of a list using the `reverse` method.
# Note that this method modifies the list in place, meaning it doesn't
# return a new list. It just changes the order of the list you call it on.
shopping_list.reverse()
shopping_list  # ['butter', 'cheese', 'bagels']


# If you want to reverse a list without modifying the original list, you
# can use the `reversed` function.
reversed_shopping_list = shopping_list.reversed()

# You can also sort a list using the `sort` method.
# Note that this method modifies the list in place, meaning it doesn't
# return a new list. It just changes the order of the list you call it on.
# Also note that you can't sort a list that contains both strings and
# numbers.
shopping_list.sort()
shopping_list  # ['bagels', 'butter', 'cheese']

# "Methods" like `append`, `pop`, `remove`, `reverse`, and `sort` are
# functions that are built into Python lists. Did you notice a pattern in
# the way we call these functions? We call them using dot notation: <list>.<method>().
#
# There are more list methods. You can read about them here:
# https://docs.python.org/3/library/stdtypes.html#list


""" Tuples """
# Tuples are a lot like lists, but they're immutable, meaning they can't
# be modified.

classes = ("Math", "English", "Science", "History")

# You can access items in a tuple using their index, just like a list.
classes[2]  # 'Science'
classes[-1]  # 'History'
classes[1:3]  # ('English', 'Science')

# But you can't modify a tuple.
# classes[1] = "Spanish" #! TypeError: 'tuple' object does not support item assignment

# There are only a few methods available for tuples.
# You can find the index of an item in a tuple using the `index` method.
classes.index("Science")  # 2

# You can count the number of times an item appears in a tuple using the
# `count` method.
tuple_with_dups = (1, 2, 3, 2, 1, 2, 3, 2, 1)
tuple_with_dups.count(2)  # 4

""" Dictionaries """
# Dictionaries are a lot like lists, but instead of using indices to
# access items, you use keys.

# Here's one way to create a dictionary:
user = {
    "first_name": "John",
    "last_name": "Buck",
    "age": 14,
    "is_active": True,
    "favorite_colors": ["blue", "green"],
}

# Here's another way:
student = dict(
    first_name="John",
    last_name="Buck",
    age=14,
    is_active=True,
    favorite_colors=["blue", "green"],
)

# You can access items in a dictionary using their keys.
student["first_name"]  # 'John'

# Dictionaries also have a special `get` method that you can use to access items.
student.get("age")  # 14

# You can add a key to a dictionary by assigning a value to it.
student["grade_level"] = 9
student.get("grade_level")  # 9

# Or you can use the `update` method.
student.update({"gpa": 3.5})
student.get("gpa")  # 3.5

# You can update the value of a key using the same syntax.
student["grade_level"] = 10
student.update({"gpa": 3.8})

# You can remove a key from a dictionary using the `pop` method.
"grade_level" in student  # True
student.pop("grade_level")
"grade_level" in student  # False

# Or you can use the `del` keyword.
del student["gpa"]
"gpa" in student  # False

# We've already seen a few dictionary methods like `get`, `update`, and `pop`,
# but there are more. What do you think each of the following does? Can you
# create an example to test your guess?
#   - keys()
#   - values()
#   - items()
#   - fromkeys()
#   - copy()
#   - clear()
