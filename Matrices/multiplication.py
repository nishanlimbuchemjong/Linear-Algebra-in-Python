"""
Matrix Multiplication
    Matrix multiplication is a fundamental operation in mathematics that involves multiplying two or more 
    matrices according to specific rules. 
    Understanding how to multiply matrices is crucial for solving various mathematical problems.

Rules and Conditions for Matrix Multiplication:
    If “A = [aij]mxn” and “B = [bij]nxo” are two matrices, 
    then the product of A and B is denoted as AB, whose order is “m x o”.
    And column of A (n) and row of matrix B (n) should be equal for matrix Multiplication

"""
def matrix_multiplication(matrix1, matrix2):

    # checking the column of matrix1 and row of matrix2; if they are equal then multiplication is possible else not
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Multiplication cannot be done. As column of matrix A and row of matrix B are unequal")
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# initializing the matrices
matrix1 = [
    [1, 8, 3],
    [9, 4, 5],
    [6, 2, 7]
]
matrix2 = [
    [6, 7, 4],
    [1, 3, 2],
    [5, 9,  8]
]

# calling the function for multiplying matrices:
result = matrix_multiplication(matrix1, matrix2)

# printing the result:
print("Matrix A:")
for i in matrix1:
    print(i)
print("\nMatrix B:")
for i in matrix2:
    print(i)
print("\nMatrix Multiplication:")
for row in result:
    print(row)