"""
Matrix Subtraction:
    Matrix subtraction is an operation where corresponding elements of two matrices are 
    subtracted from each other to form a new matrix. This operation is similar to matrix addition, 
    but instea

    For two matrices to be subtracted, they must have the same dimensions, meaning they must have 
    the same number of rows and columns. If A and B are two matrices of the same dimensions, 
    their subtraction is denoted as A - B.
"""
def matrix_subtraction(matrix1, matrix2):

    # cheking if the matrices have same dimensions or not
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix1[0]):
        raise ValueError("Matrices should have same dimensions")
    
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# initializing the matrices
matrix1 = [
    [1, 2, 3],
    [4, -1, -2]
]
matrix2 = [
    [-1, 2, -3],
    [2, 0, 1]
]

# calling the function for subtracting matrices:
result = matrix_subtraction(matrix1, matrix2)

# printing the result:
print("Matrix A:")
for i in matrix1:
    print(i)
print("\nMatrix B:")
for i in matrix2:
    print(i)
print("\nMatrix Subtraction:")
for row in result:
    print(row)