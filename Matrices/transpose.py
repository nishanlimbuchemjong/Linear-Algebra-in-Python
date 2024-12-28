"""
Transpose of a Matrix:
    Transpose of a matrix is a matrix that is obtained by swapping the rows and columns of the given matrix 
    or vice versa, i.e., for the given matrix the elements in rows are interchanged with the elements in columns. For any given matrix A its transpose is denoted as At, or AT.
"""
def transpose_matrix(matrix):
    transpose = []
    for col in range(len(matrix[0])):
        row = []
        for row_matrix in matrix:
            row.append(row_matrix[col])
        transpose.append(row)
    return transpose

matrix = [
    [1, 2],
    [3, 4],
    [2, 6],
]

result = transpose_matrix(matrix)

print("Matrix A: ")
for i in matrix:
    print(i)
print("\nTranspose Matrix :")
for i in result:
    print(i)
