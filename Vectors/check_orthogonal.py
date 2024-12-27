"""
Given two vectors:
    p = [2, -1, 3]
    q = [-6, 3, -9]
Check the two vectors are othogonal or not?

[Note: if the dot product == 0 then orthogonal else not orthogonal]

"""
p = [2, -1, 3]
q = [-6, 3, -9]

# finding the dot product of the given two vectors:
dot_product = sum(p[i] * q[i] for i in range(len(p)))

# checking for orthogonal or not:
if (dot_product == 0):
    print(f"{p} and {q} vectors are Orthogonal")
else:
    print(f"{p} and {q} vectors are not Orthogonal")