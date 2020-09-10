# def luhn_test(x):
#     x = [int(i) for i in x]
#     even = [i * 2 for i in x[-2::-2]]
#     even = [i - 9 if i > 9 else i for i in even]
#     odd = [i for i in x[-3::-2]]
#     s = sum(even) + sum(odd) + x[-1]
#     return s % 10 == 0
#
# print(luhn_test("4000003414116814"))
# print(int('323.03'))
res_matrix = [[1, 2], [3, 4]]
for i in res_matrix:
    print(" ".join([str(_) for _ in i]), sep=' ')
