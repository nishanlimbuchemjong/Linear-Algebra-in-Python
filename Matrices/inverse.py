"""
Inverse of a Matrix:
    The inverse of a Matrix is the matrix that on multiplying with the original matrix results in 
    an identity matrix. 
    For any square matrix A, its inverse is denoted as A^-1.  
    The inverse of a matrix is obtained by dividing the adjugate of the given matrix by the determinant 
    of the given matrix.

"""
def get_minor_matrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] *  matrix[1][1] -  matrix[1][0] *  matrix[0][1]
    
    det = 0

    for col in range(len(matrix)):
        det += ((-1)**col * matrix[0][col] * determinant(get_minor_matrix(matrix, 0, col)))
    
    return det

def inverse(matrix):
    det = determinant(matrix)

    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    
    cofactor = []

    for row in range(len(matrix)):
        cofactor_row = []
        for col in range(len(matrix)):
            minor = get_minor_matrix(matrix, row, col)
            cofactor_row.append(((-1)**(row+col))*determinant(minor))
        cofactor.append(cofactor_row)
    
    cofactor = list(map(list, zip(*cofactor)))

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            cofactor[row][col] /= det
    
    return cofactor

matrix = [
    [1, 2, -2],
    [-1, 3, 0],
    [0, -2, 1]
]

result = inverse(matrix)
print(f"Inverse of matrix A = {matrix} is given below:")
for row in result:
    print(row)