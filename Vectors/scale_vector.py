"""
Scale Vector:
    A scaled vector is a vector that has been resized (increased or decreased in magnitude) by multiplying 
    all of its components by a scalar value. 
    
    Scaling a vector changes its magnitude (length) but does not affect its direction unless 
    the scalar is negative, in which case the vector also reverses direction.

Mathematical Definition:
    If we have a vector v = [v1, v2, v3], scaling it by a scalar k results in a new vector:
        kv = [k⋅v1, k⋅v2, k⋅v3]
    where,
        k is a scalar
        v is the original vector
        kv is the scaled vector

Key Points
    Magnitude: Scaling changes the vector's length (magnitude).
        If |k|>1, the vector becomes longer.
        If |k|<1, the vector becomes shorter.
        If k=0, the vector becomes a zero vector (magnitude = 0).
    Direction:
        If k>0, the direction of the vector remains the same.
        If k<0, the direction of the vector is reversed.

"""
def scalar_vector(v, scalar):
    scalr_vector_result = [scalar * v[i] for i in range(len(v))]
    return scalr_vector_result

v = [2, 3]
scalar = 2
result = scalar_vector(v, scalar)

print(f"Scaled Vector of vector {v} where scalar(k) = {scalar} is {result}")