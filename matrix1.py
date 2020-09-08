# col1, row1 = input().split(' ')
# col1, row1 = int(col1), int(row1)
# matrix1 = input()
#
# col2, row2 = input().split(' ')
# col2, row2 = int(col2), int(row2)
# matrix2 = input()
col = 3
row = 3
mtr = '''1 2 3
4 5 6
7 8 9'''
matrix = mtr.split('\n') #["1 2 3", "4 5 6", "7 8 9"]
matrix1 = [i.split(' ') for i in matrix]
print(matrix1)
# def str_to_matrix_int(col, row, matrix):
#
#     return out_matrix


# print(str_to_matrix_int(2, 2, '1 2 3 4'))
# print([[] for i in range(2)]) #--> [[], []]
# print([[] for i in range(3)]) #--> [[], [], []]