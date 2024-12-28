"""
Determinant of Matrix:
    Determinant of Matrix is defined as the sum of products of the elements of any row or column
    along with their corresponding co-factors. 
    The determinant is defined only for square matrices of any order 2x2, 3x3, 4x4, or n x n, 
    where n is the number of rows or the number of columns.
"""    
def determinant(matrix):
    # for 2 X 2 matrix
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0

    # calculating the determinant usig recursive
    for col in range(len(matrix)):
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += (-1)**col * matrix[0][col] * determinant(submatrix)
    
    return det

# initial matrix
matrix1 = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

# calling the determinant function
result = determinant(matrix1)

# printing the result
print(f"Determinant of matrix A = {matrix1}: {result}")