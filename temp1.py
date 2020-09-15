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


# res_matrix = [[1, 2], [3, 4]]
# for i in res_matrix:
#     print(" ".join([str(_) for _ in i]), sep=' ')


vowels = {'a', 'e', 'i', 'o', 'u'}


def find_apostrophe(word, start):
    i = word.index("'", start)

    if i == -1:
        print("1")
        return -1

    if i == 0:
        print("2")
        return find_apostrophe(word, 1)

    elif i == len(word) - 1:
        print("3")
        return -1

    else:
        previous_char = word[i - 1]
        if previous_char in set(vowels):
            print("4")
            return i

        else:
            print("5")
            return find_apostrophe(word, i + 1)

correct_index = find_apostrophe("'w'ord'", 0)
print(correct_index)