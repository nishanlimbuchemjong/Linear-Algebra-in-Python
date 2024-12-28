"""
Symmetric Matrix:
    A square matrix A = (aij) is called a symmetric matrix, if its (i, j)th element is equal to its (j, i)th element, i.e. if aij = aji

"""
def checking_symmetric(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

matrix = [
    [1, 3, 7],
    [3, 0, -6],
    [7, -6, 8]
]

result = checking_symmetric(matrix)
if result == True:
    print(f"Given matrix is a Symmetric Matrix")
else:
    print(f"Given matrix is not a Symmetric Matrix")