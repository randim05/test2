matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res_matrix = [[] for i in range(len(matrix1[0]))]
# if col1 == row2:
for i in range(3):  # range(len(matrix1[0])-1):
    for j in range(3):  # range(len(matrix2)-1):
        for k in range(3):  # range(len(matrix1[0])-1):
            if not k:
                res_matrix[i].append(0)
            else:
                res_matrix[i][j] = res_matrix[i][j] + \
                                matrix1[i][j] * matrix2[i + k][j]
print(res_matrix)