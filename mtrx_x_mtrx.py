matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res_matrix = [[0 for i in range(len(matrix2))] for j in range(len(matrix1[0]))]
# if col1 == row2:
for i in range(len(matrix1)):  # range(len(matrix1[0])-1):
    for j in range(len(matrix2[0])):  # range(len(matrix2)-1):
        for k in range(len(matrix1[0])):  # range(len(matrix1[0])-1):
            res_matrix[i][j] = res_matrix[i][j] + \
                                matrix1[i][k] * matrix2[k][j]
print(res_matrix)