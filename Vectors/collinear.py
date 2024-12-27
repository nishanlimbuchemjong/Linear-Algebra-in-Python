"""
Collinear Vectors
    Two or more vectors are said to be collinear if they lie along the same straight line.

Check for Collinearity (Cross Product Method):
    Two vectors v1 and v2 are collinear if their cross product is the zero vector:
        v1 X v2 = 0
    If the cross product results in a zero vector, then the vectors are collinear, meaning they lie on the same straight line.
"""
"""
Q. Given to vectors:
    v1 = (2, 4, 6); and v2 = (1, 2, 3)
    prove that given two vectors are collinear.

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

v1 = (2, 4, 6)
v2 = (1, 2, 3)

# calling the cross_product function:
result = cross_product(v1, v2)

# checking given two vectors are collinear or not:
if result == 0:
    print(f"{v1} and {v2} vectors are collinear")
else:
    print(f"{v1} and {v2} vectors are not collinear")