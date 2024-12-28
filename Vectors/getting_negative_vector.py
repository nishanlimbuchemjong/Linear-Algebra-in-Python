"""
Negative Vector:
    A vector having the same magnitude as that of a given vector OP but direction opposite to it and denoted by vector -OP or vector PO is called the negative of vector OP

"""
def negative_vector(v):
    neg_vector = []
    for i in range(len(v)):
        neg_vector.append(-v[i])

    return neg_vector

# initial vector
v = [1, 10, -5]

# calling the function
result = negative_vector(v)

# Printing the result
print(f"Negative vector of {v} = {result}")