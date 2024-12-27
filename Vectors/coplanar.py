"""
Coplanar Vectors:
    Three or more vectors are said to be coplanar if they lie within the same plane. 
    This means that the vectors do not span more than two dimensions, and we can find a plane that contains all of them.

Mathematically:
    Three vectors v1, v2, and v3 are coplanar if the scalar triple product of these vectors is zero. 
   
    The scalar triple product is calculated as:
        v1 ⋅ (v2 X v3) = 0
    
    If this value is zero, then the vectors are coplanar. 
    If it is non-zero, the vectors are not coplanar (they span a 3D space).
"""
"""
Q. Given three vectors:
            v1 = (1, 2, 3);      v2 = (4, 5, 6);    v3 = (7, 8, 9)
    Prove that the given three vectors are coplanar
"""
def cross_product(v2, v3):
    x1, y1, z1 = v2
    x2, y2, z2 = v3

    # formula to calculate the cross product
    cross_product_result = (
        (y1*z2 - z1*y2),
        (z1*x2 - x1*z2),
        (x1*y2 - y1*x2)
    )

    return cross_product_result

v1 = (1, 2, 3)
v2 = (4, 5, 6)
v3 = (7, 8, 9)

# calling the cross_product function
result = cross_product(v2, v3)

# calculating the dot product between v1 and result
dot_product = sum(v1[i] * result[i] for i in range(len(result)))

# checking the given three vectors are coplanar or not:
if dot_product == 0:
    print(f"{v1}, {v2}, and {v3} vectors are coplanar vector")
else:
    print(f"{v1}, {v2}, and {v3} vectors are not coplanar vector")