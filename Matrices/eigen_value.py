def subtract_lambda(matrix, lam):
    return [[matrix[i][j] - (lam if i == j else 0) for j in range(len(matrix))] for i in range(len(matrix))]

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    det = 0

    for col in range(len(matrix)):
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1)**col * matrix[0][col] * determinant(minor))
    return det

def find_eigen_value(matrix):
    eigenvalue = []
    for lam in range(-100, 101):
        modified_matrix = subtract_lambda(matrix, lam)
        if determinant(modified_matrix) == 0:
            eigenvalue.append(lam)
    return eigenvalue

matrix = [
    [4, 1],
    [2, 3]
]

result = find_eigen_value(matrix)
print("Result: ", result)