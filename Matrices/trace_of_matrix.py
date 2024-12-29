"""
Trace of Matrix:
    It is the sum of diagonal elements of the matrix.
    Mathematically, 
        Tr(A) = a11 + a22 + a33 + .......+ anm
"""

def trace_of_matrix(matrix):
    # checking given matrix is squared matrix or not
    if len(matrix) != len(matrix[0]):
        raise ValueError("Must be a squared matrix.")
    
    tr_matrix = 0

    # adding all the diagonal
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                tr_matrix += matrix[i][j]
    
    return tr_matrix

# initializating matrix
matrix = [
    [20, 0, 5],
    [0, 2, 5],
    [-7, 2, 5]
]

# calling the funciton
result = trace_of_matrix(matrix)

# printing the result
print(f"Trace of given matrix = {result}")