"""
Singular Matrix:
A square matrix is said to be a singualr matrix if its determinat is zero.
Otherwise, the square matrix is said to be non-singular. 

"""
def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    
    det = 0

    for col in range(len(matrix)):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += (-1)**col * matrix[0][col] * determinant(sub_matrix)
    
    return det

#  initial matrix
matrix = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

result = determinant(matrix)

if result == 0:
    print(f"Given matrix is Singular matrix")
else:
    print(f"Given matrix is Non-Singular matrix")