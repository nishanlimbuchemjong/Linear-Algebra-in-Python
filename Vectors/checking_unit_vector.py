"""
Unit Vector:
    A unit vector is a vector whose magnitude is unity. So if vector a = 1 then vector a is said to be a unit vector.
    The example of unit vectors are (1, 0) and (0, 1)
"""
import math
def checking_unity(v):

    value = 0

    for i in range(len(v)):
        value += v[i]**2
    
    vector_value = math.sqrt(value)
    return vector_value

v = [1, 0, 0]
result = checking_unity(v)
if result == 1:
    print("Given vector is an unit vector")
else:
    print("Given vector is not an unit vector")
