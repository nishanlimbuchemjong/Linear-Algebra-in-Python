"""
Given two vectors:
    a = [3, 4, 5]; b = [1, 0, -1]
Find a dot product a dot b

Here, numpy library is not used.
"""
# defining two vectors
a = [3, 4, 5]
b = [1, 0, -1]

dot_product = sum(a[i] * b[i] for i in range(len(a)))

print(f"Dot product of a = {a} and b = {b} is {dot_product}")