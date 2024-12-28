"""
Skew-symmetric Matrix:
    A square matrix A = (aij) is called a skew-symmetric matrix, 
    if its (i, j)th element is the negative of its (j, i)th element, i.e. if aij = - aji
    
"""

def checking_skew_symmetric(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -matrix[j][i]:
                return False
    
    return True

# initial matrix:
matrix = [
    [0, 5, -7],
    [-5, 0, 3],
    [7, -3, 0]
]

result = checking_skew_symmetric(matrix)

if result == True:
    print("Given matrix is a skew-symmetric matrix")
else:
    print("Given matrix is not a skew-symmetric matrix")