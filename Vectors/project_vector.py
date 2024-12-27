"""
Vector Projection is a method of finding component of a vector along the direction of second vector.

By projecting a vector on another vector we obtain a vector which represent the component of the first vector 
along the direction of second vector. It represent the length of the shadow of a vector over another vector.

Question:
Two vectors:
    a = [3, 4, 5]
    b = [6, 8, 10]
Projection of vector a on vector b = ?
Projection of vector b on vector a = ?

[Hint: Formulas,
        Projection of vector a on vector b = (a*b) / |b|
        Projection of vector b on vector a = ()a*b) / |a|
]
"""
import math 
a = [4, 2, 1]
b = [5, -3, 3]

# finding dot product of vector a and vector b:
dot_product = sum(a[i] * b[i] for i in range(len(a)))

# finding the magnitude of vector a and vector b:
magnitude_a = math.sqrt(sum((a[i])**2 for i in range(len(a))))
magnitude_b = math.sqrt(sum((b[i])**2 for i in range(len(b))))

# finding the projection of vector a on vector b; Also projection of vector b on vector a:
project_a_on_b = dot_product / magnitude_b
project_b_on_a = dot_product / magnitude_a

# printing the result:
print(f"Projection of vector a = {a} on vector b = {b} is {project_a_on_b: .4f}")
print(f"Projection of vector a = {a} on vector b = {b} is {project_b_on_a: .4f}")