from average import mean, median, mode

def test(fn, list, expected):
    result = fn(list)
    if result == expected:
        print(f"✅ The {fn.__name__} of {list} is {result}")
    else:
        print(f"❌ The {fn.__name__} of {list} isn't {result}, expected {expected}")

test(mean, [1, 2, 3, 4, 5], 3)
test(mean, [1, 2, 3, 4, 5, 6], 3.5)
test(mean, [3, 4.5, 19, 27, 100], 30.7)
test(median, [1, 2, 3, 4, 5], 3)
test(median, [1, 2, 3, 4, 5, 6], 3.5)
test(median, [4, 1, 7, 3, 6], 4)
test(median, [6, 1, 4, 2, 5, 3], 3.5)
test(mode, [1, 2, 3, 4, 5, 2], 2)
test(mode, [3, 3, 1, 1], 3)
test(mode, [1, 2, 3, 4, 5], 1)
test(mode, ["red", "blue", "green", "blue"], "blue")
