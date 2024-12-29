def solve_homogeneour(matrix):
    solution = [0] * len(matrix)
    solution[0] = 1
    for i in range(1, len(matrix)):
        if matrix[i][i-1] != 0:
            solution[i] = -matrix[i][i-1] / matrix[i-1][i-1]
        else:
            solution[i] = 1
    return solution

def subtract_lambda(matrix, lam):
    return [[matrix[i][j] - (lam if i==j else 0) for j in range(len(matrix))] for i in range(len(matrix))]

def find_eigen_vector(matrix, eigen_value):
    eigenvector = {}
    for lam in eigen_value:
        modified_matrix = subtract_lambda(matrix, lam)
        eigenvector[lam] = solve_homogeneour(modified_matrix)
    return eigenvector

matrix = [
    [1, 2],
    [5, 4]
]

eigenvalues = [6, -1]

result = find_eigen_vector(matrix, eigenvalues)

for lam, vect in result.items():
    print(f"eigen values- {lam}: eigen vector {vect}")