from area import (
    area_square, 
    area_rectangle, 
    area_triangle, 
    area_circle, 
    bonus_area_rectangle
)

def test(fn, args, expected):
    result = fn(*args)
    if result == expected:
        print(f"✅ Function {fn.__name__} called with arg(s) ({', '.join(map(str, args))}) returned {result}")
    else:
        print(f"❌ Function {fn.__name__} called with arg(s) ({', '.join(map(str, args))}) returned {result}, expected {expected}")

test(area_square, [5], 25)
test(area_rectangle, [5, 3], 15)
test(area_rectangle, [10, 10], 100)
test(area_rectangle, [2.5, 4.25], 10.625)
test(area_triangle, [3, 4], 6)
test(area_triangle, [5, 5], 12.5)
test(area_circle, [5], 78.53981633974483)
test(area_circle, [10], 314.1592653589793)
test(bonus_area_rectangle, [5], 25)
test(bonus_area_rectangle, [10, 5], 50)
