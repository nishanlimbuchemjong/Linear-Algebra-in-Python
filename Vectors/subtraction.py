"""
Given:
    a = [1, 2, 3]
    b = [4, 5, 6]
Vector addition of 2a - 3b = ?

"""
a = [1, 2, 3]
b = [4, 5, 6]

# calculating the subtraction using list comprehension:
subtraction = [2*a[i] - 3*b[i] for i in range(len(a))]

# printing the result:
print(f"Subtraction: {subtraction}")
