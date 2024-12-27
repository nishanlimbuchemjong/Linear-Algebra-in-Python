"""
Given:
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
find the cross product of two vectors v1 and v2?

[Hint:
    a X b = a2b3 - a3b2,  a3b1-a1b3, a1b2 - a2b1
]
"""
def cross_product(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2

    # formula to calculate the cross product
    cross_product_result = (
        (y1*z2 - z1*y2),
        (z1*x2 - x1*z2),
        (x1*y2 - y1*x2)
    )

    return cross_product_result


v1 = (1, 2, 3)
v2 = (4, 5, 6)

# calling the cross_product function:
result = cross_product(v1, v2)

# printing the result
print(f"Cross product of {v1} and {v2} is {result}")