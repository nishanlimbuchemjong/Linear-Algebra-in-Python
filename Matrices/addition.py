"""
Matrix Addition:
    A matrix is a rectangular array or set of elements. 
    The Matrix can be defined as an m×n element in the form of m horizontal lines (rows), 
    and n vertical lines (columns) known as the m*n order matrix. Elements can be real, complex, or unknown numbers

    Matrix addition is the operation defined on the matrix to add two matrices to get a single matrix. 
    Let’s suppose two matrices A and B, such A = [aij] and B = [bij], 
    then their addition A + B is defined as [aij + bij], 
    where ij represents the element in ith row and jth column.

"""

def matrix_addition(matrix1, matrix2):
    # checking if matrices have same dimensions or not:
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
        
    result = []

    # adding the matrixces
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

# initializing the matrices
matrix1 = [
    [1, 2, 3],
    [-3, 4, 1]
]
matrix2 = [
    [1, -2, 3],
    [4, 4, -7]
]

# calling the function for addding matrices:
result = matrix_addition(matrix1, matrix2)

# printing the result:
# printing the matrix A
print("Matrix A:")
for i in matrix1:
    print(i)

# printing the matrix B
print("\nMatrix B:")
for i in matrix2:
    print(i)

# printing result after addition
print("\nMatrix Addition:")
for row in result:
    print(row)