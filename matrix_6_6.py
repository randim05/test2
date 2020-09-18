def transposeMatrix(m):
    return map(list, zip(*m))


def getMatrixMinor(m, x, y):
    return [row[:y] + row[y + 1:] for row in (m[:x] + m[x + 1:])]


def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
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


def print_m(m):
    for i in m:
        print(" ".join([str(_) for _ in i]), sep=' ')


martix = [[2, -1, 0], [0, 1, 2], [1, 1, 0]]
mtr = transposeMatrix(martix)
mm00 = getMatrixMinor(martix, 0, 0)
det = getMatrixDeternminant(martix)
matrix_1 = getMatrixInverse(martix)

for i in (mtr, mm00, det, matrix_1):
    print_m(i)
