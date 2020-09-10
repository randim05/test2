user_choice = "75"

while user_choice != "0":
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
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

