cr1 = input().split(' ')
row1, col1 = int(cr1[0]), int(cr1[1])
matrix1 = []
i = 0
while i < row1:
    matrix1.append(input().split(' '))
    i += 1
c = int(input())
# cr2 = input().split(' ')
# row2, col2 = int(cr2[0]), int(cr2[1])
# matrix2 = []
# i = 0
# while i < row2:
#     matrix2.append(input().split(' '))
#     i += 1

# res_matrix = [[] for i in range(row1)]
# if col1 == col2 and row1 == row2:
#     for i in range(row1):
#         for j in range(col1):
            # res_matrix[i].append(str(int(matrix1[i][j]) + int(matrix2[i][j])))

# else:
#     print("ERROR")
# print(res_matrix)
# res_matrix = [[str(c*int(matrix1[i][j])) for i in range(row1)] for j in range(col1)]
res_matrix = []
for i in matrix1:
    res_matrix.append([str(int(j) * c) for j in i])
for i in res_matrix:
    print(' '.join(i))
