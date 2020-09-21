user_choice = "75"
import  math
def find_det(matrix, mul=1):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        summa = 0
        for x in range(width):
            m = []
            for y in range(1, width):
                buff = []
                for z in range(width):
                    if z != i:
                        buff.append(matrix[y][z])
                m.append(buff)
            sign *= -1
            summa += mul * find_det(m, sign * matrix[0][x])
        return summa

def transposeMatrix(mtr):
    # return map(list, zip(*mtr))
    rm = [[0 for x in range(len(mtr[0]))] for y in range(len(mtr))]
    for x in range(len(mtr)):
        for y in range(len(mtr[0])):
            rm[x][y] = mtr[y][x]
    return rm


def getMatrixMinor(m, x, y):
    return [row[:y] + row[y + 1:] for row in (m[:x] + m[x + 1:])]


def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    elif len(m) == 3:
        return m[0][0] * m[1][1] * m[2][2] + \
               m[1][0] * m[0][2] * m[2][1] + \
               m[2][0] * m[0][1] * m[1][2] - \
               m[2][0] * m[1][1] * m[0][2] - \
               m[0][0] * m[2][1] * m[1][2] - \
               m[1][0] * m[0][1] * m[2][2]
    else:
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(
                getMatrixMinor(m, 0, c))
        return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]
    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactor_row = []
        for u in range(len(m)):
            minor = getMatrixMinor(m, r, u)
            cofactor_row.append(
                ((-1) ** (r + u)) * getMatrixDeternminant(minor))
        cofactors.append(cofactor_row)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for u in range(len(cofactors)):
            cofactors[r][u] = cofactors[r][u] / determinant
    return cofactors

# def matrix_x_c(mtr, w):
#     rm = []
#     for x in mtr:
#         rm.append([y * w for y in x])
#     return rm
#
#
# def matrix_x_matrix(mtr1, mtr2):
#     rm = [[0 for x in range(len(mtr2[0]))] for y in range(len(mtr1))]
#     for x in range(len(mtr1)):
#         for y in range(len(mtr2[0])):
#             for z in range(len(mtr2)):
#                 rm[x][y] = rm[x][y] + mtr1[x][z] * mtr2[z][y]
#     return rm
#
#
# def matrix_transpose(mtr):
#     rm = [[0 for x in range(len(mtr[0]))] for y in range(len(mtr))]
#     for x in range(len(mtr)):
#         for y in range(len(mtr[0])):
#             rm[x][y] = mtr[y][x]
#     return rm


# def martix_invers(mtr):


while user_choice != "0":
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    if user_choice == "75":
        user_choice = input("Your choice: ")
        # continue
    else:
        user_choice = input("Your choice: ")
    if len(user_choice) > 1:
        continue
    elif user_choice == "1":
        cr1 = input("Enter size of first matrix: ").split(' ')
        row1, col1 = int(cr1[0]), int(cr1[1])
        matrix1 = []
        i = 0
        print("Enter first matrix:")
        while i < row1:
            matrix1.append(input().split(' '))
            try:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = int(matrix1[i][j])
            except ValueError:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = float(matrix1[i][j])

            i += 1
        cr2 = input("Enter size of second matrix: ").split(' ')
        row2, col2 = int(cr2[0]), int(cr2[1])
        matrix2 = []
        i = 0
        print("Enter second matrix:")
        while i < row2:
            matrix2.append(input().split(' '))
            try:
                for j in range(len(matrix2[i])):
                    matrix2[i][j] = int(matrix2[i][j])
            except ValueError:
                for j in range(len(matrix2[i])):
                    matrix2[i][j] = float(matrix2[i][j])
            i += 1
        res_matrix = [[] for i in range(row1)]
        if col1 == col2 and row1 == row2:
            for i in range(row1):
                for j in range(col1):
                    res_matrix[i].append(
                        matrix1[i][j] + matrix2[i][j])
            print("The result is:")
            for i in res_matrix:
                print(" ".join([str(_) for _ in i]), sep=' ')
        else:
            print("The operation cannot be performed.")

    elif user_choice == "2":
        cr1 = input("Enter size of matrix: ").split(' ')
        row1, col1 = int(cr1[0]), int(cr1[1])
        matrix1 = []
        i = 0
        print("Enter matrix:")
        while i < row1:
            matrix1.append(input().split(' '))
            try:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = int(matrix1[i][j])
            except ValueError:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = float(matrix1[i][j])
            i += 1
        c = int(input("Enter constant: "))
        res_matrix = []
        for i in matrix1:
            res_matrix.append([j * c for j in i])
        print("The result is:")
        for i in res_matrix:
            print(" ".join([str(_) for _ in i]), sep=' ')

    elif user_choice == "3":
        cr1 = input("Enter size of first matrix: ").split(' ')
        row1, col1 = int(cr1[0]), int(cr1[1])
        matrix1 = []
        i = 0
        print("Enter first matrix:")
        while i < row1:
            matrix1.append(input().split(' '))
            try:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = int(matrix1[i][j])
            except ValueError:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = float(matrix1[i][j])
            i += 1
        cr2 = input("Enter size of second matrix: ").split(' ')
        row2, col2 = int(cr2[0]), int(cr2[1])
        matrix2 = []
        i = 0
        print("Enter second matrix:")
        while i < row2:
            matrix2.append(input().split(' '))
            try:
                for j in range(len(matrix2[i])):
                    matrix2[i][j] = int(matrix2[i][j])
            except ValueError:
                for j in range(len(matrix2[i])):
                    matrix2[i][j] = float(matrix2[i][j])
            i += 1
        res_matrix = [[0 for i in range(col2)] for j in range(row1)]
        if col1 == row2:
            for i in range(row1):
                for j in range(col2):
                    for k in range(row2):
                        res_matrix[i][j] = res_matrix[i][j] + \
                                        matrix1[i][k] * matrix2[k][j]

        else:
            print("The operation cannot be performed.")
        # for i in matrix1:
        #     res_matrix.append([str(int(j) * c) for j in i])
        for i in res_matrix:
            print(" ".join([str(_) for _ in i]), sep=' ')
    elif user_choice == '0':
        break
    elif user_choice == '4':
        print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        user_choice_trans = input("Your choice: ")
        if user_choice_trans == "1":
            cr1 = input("Enter matrix size: ").split(' ')
            row1, col1 = int(cr1[0]), int(cr1[1])
            matrix1 = []
            i = 0
            print("Enter matrix:")
            while i < row1:
                matrix1.append(input().split(' '))
                try:
                    for j in range(len(matrix1[i])):
                        matrix1[i][j] = int(matrix1[i][j])
                except ValueError:
                    for j in range(len(matrix1[i])):
                        matrix1[i][j] = float(matrix1[i][j])
                i += 1
            res_matrix = [[0 for i in range(col1)] for j in range(row1)]

            for i in range(row1):
                for j in range(col1):
                    res_matrix[i][j] = matrix1[j][i]
            print("The result is:")
            for i in res_matrix:
                print(" ".join([str(_) for _ in i]), sep=' ')
        elif user_choice_trans == "2":
            cr1 = input("Enter matrix size: ").split(' ')
            row1, col1 = int(cr1[0]), int(cr1[1])
            matrix1 = []
            i = 0
            print("Enter matrix:")
            while i < row1:
                matrix1.append(input().split(' '))
                try:
                    for j in range(len(matrix1[i])):
                        matrix1[i][j] = int(matrix1[i][j])
                except ValueError:
                    for j in range(len(matrix1[i])):
                        matrix1[i][j] = float(matrix1[i][j])
                i += 1
            res_matrix = [[0 for i in range(col1)] for j in range(row1)]
            k = row1 - 1
            for i in range(row1):
                for j in range(col1):
                    res_matrix[i][j] = matrix1[k - j][k - i]
            print("The result is:")
            for i in res_matrix:
                print(" ".join([str(_) for _ in i]), sep=' ')
        elif user_choice_trans == "3":
            cr1 = input("Enter matrix size: ").split(' ')
            row1, col1 = int(cr1[0]), int(cr1[1])
            matrix1 = []
            i = 0
            print("Enter matrix:")
            while i < row1:
                matrix1.append(input().split(' '))
                try:
                    for j in range(len(matrix1[i])):
                        matrix1[i][j] = int(matrix1[i][j])
                except ValueError:
                    for j in range(len(matrix1[i])):
                        matrix1[i][j] = float(matrix1[i][j])
                i += 1
            res_matrix = []
            for i in matrix1:
                i.reverse()
                res_matrix.append(i)
            print("The result is:")
            for i in res_matrix:
                print(" ".join([str(_) for _ in i]), sep=' ')
        elif user_choice_trans == "4":
            cr1 = input("Enter matrix size: ").split(' ')
            row1, col1 = int(cr1[0]), int(cr1[1])
            matrix1 = []
            i = 0
            print("Enter matrix:")
            while i < row1:
                matrix1.append(input().split(' '))
                try:
                    for j in range(len(matrix1[i])):
                        matrix1[i][j] = int(matrix1[i][j])
                except ValueError:
                    for j in range(len(matrix1[i])):
                        matrix1[i][j] = float(matrix1[i][j])
                i += 1
            matrix1.reverse()
            res_matrix = matrix1
            print("The result is:")
            for i in res_matrix:
                print(" ".join([str(_) for _ in i]), sep=' ')
    elif user_choice == '5':
        cr1 = input("Enter matrix size: ").split(' ')
        row1, col1 = int(cr1[0]), int(cr1[1])
        matrix1 = []
        i = 0
        print("Enter matrix:")
        while i < row1:
            matrix1.append(input().split(' '))
            try:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = int(matrix1[i][j])
            except ValueError:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = float(matrix1[i][j])
            i += 1
        # res_matrix = getMatrixDeternminant(matrix1)
        if row1 == 1 and col1 == 1:
            res_matrix = matrix1[0][0]
        elif row1 == 1 and col1 > 1:
            res_matrix = matrix1[0][0]
        else:
            res_matrix = getMatrixDeternminant(matrix1)
        if res_matrix:
            print("The result is:")
            print(res_matrix)
        else:
            print("Matrix not consistents")
        # for i in res_matrix:
        #     print(" ".join([str(_) for _ in i]), sep=' ')
    elif user_choice == '6':
        cr1 = input("Enter size of first matrix: ").split(' ')
        row1, col1 = int(cr1[0]), int(cr1[1])
        matrix1 = []
        i = 0
        print("Enter first matrix:")
        while i < row1:
            matrix1.append(input().split(' '))
            try:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = int(matrix1[i][j])
            except ValueError:
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = float(matrix1[i][j])
            i += 1

        res_matrix = getMatrixInverse(matrix1)
        for i in res_matrix:
            print(" ".join([str(_) for _ in i]), sep=' ')
        # print(" ".join(['%5.2f' % (round(_, 2)) for _ in i if _ not in ("-0.0", "-0", "-0.00")]), sep=' ')
        # pr_res_mtr = []
        # for i in len(res_matrix):
        #     pr_res_mtr.append([])
        #     for j in len(res_matrix[i]):
        #         if j:
        #             pr_res_mtr[i].append('%5.2f' % j)
        #         else:
        #             pr_res_mtr[i].append('%5d' % 0)
        # for i in pr_res_mtr:
        #     print("".join([_ for _ in i]), sep=' ')
