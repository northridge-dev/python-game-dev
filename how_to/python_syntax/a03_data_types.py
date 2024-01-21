"""
Besides the integers, floats, strings, and booleans we've already
seen, Python has a few common data types:
- lists
- tuples
- dictionaries

These are all "complex" data types, meaning they can store multiple
"simple" or "complex" data types.
"""

""" First: lists """
# A list is just an ordered collection of data.
# Enclose a list in square brackets, with each item separated by a comma.
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


