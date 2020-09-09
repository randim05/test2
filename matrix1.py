# # col1, row1 = input().split(' ')
# # col1, row1 = int(col1), int(row1)
# # matrix1 = input()
# #
# # col2, row2 = input().split(' ')
# # col2, row2 = int(col2), int(row2)
# # matrix2 = input()
# col = 3
# row = 3
# mtr = '''1 2 3
# 4 5 6
# 7 8 9'''
# matrix = mtr.split('\n') #["1 2 3", "4 5 6", "7 8 9"]
# matrix1 = [i.split(' ') for i in matrix]
# print(matrix1)
# # def str_to_matrix_int(col, row, matrix):
# #
# #     return out_matrix
#
#
# # print(str_to_matrix_int(2, 2, '1 2 3 4'))
# # print([[] for i in range(2)]) #--> [[], []]
# # print([[] for i in range(3)]) #--> [[], [], []]
cr1 = input().split(' ')
row1, col1 = int(cr1[0]), int(cr1[1])
matrix1 = []
i = 0
while i < row1:
    matrix1.append(input().split(' '))
    i += 1

cr2 = input().split(' ')
row2, col2 = int(cr2[0]), int(cr2[1])
matrix2 = []
i = 0
while i < row2:
    matrix2.append(input().split(' '))
    i += 1

# def str_to_matrix_int(matrix):
#     tmp_matrix = matrix.split("\n")
#     out_matrix = [i.split(" ") for i in tmp_matrix]
#     return out_matrix

# res_matrix = [[] for i in range(row1)]
# m1 = [['1', '2'], ['3', '4']]
# m2 = [['1', '2'], ['3', '4']]
res_matrix = [[] for i in range(row1)]
# print(res_matrix)
if col1 == col2 and row1 == row2:
    # matrix1 = str_to_matrix_int(matrix1)
    # matrix2 = str_to_matrix_int(matrix2)
    # for n in range(row1):
    for i in range(row1):
        for j in range(col1):
            res_matrix[i].append(str(int(matrix1[i][j]) + int(matrix2[i][j])))
else:
    print("ERROR")
print(res_matrix)
for i in res_matrix:
    print(" ".join(i))
