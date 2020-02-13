a = {1, 2, 3}
e = {1, 2, 3}

b = {1, 2, 3, 5, 6}
c = {3, 4, 5, 6}
d = {1, }

print(a - c)  # разность только те что есть в вычитаемом {1, 2}
print(c - a)  # {4, 5, 6}

print(
    a | b)  # cумма объединение все из обоих минус дубли тк множество {1, 2, 3, 5, 6}
print(b | a)  # {1, 2, 3, 5, 6}

print(a ^ b)  # xor исключающее или есть только в 1  {5, 6}
print(b ^ a)  # {5, 6}

print(a & b)  # пересечение есть в обоих {1, 2, 3}
print(b & a)  # {1, 2, 3}

# проверка на подмножество
# True если является подмножеством
# если a мн содержится полностью в b то a меньше а b больше
# во всех остальных случаях False
print(b < c)    # False
print(c < b)    # False
print(b > c)    # False
print(c > b)    # False

print(a < b)    # True
print(b < a)    # False
print(a > b)    # False
print(b > a)    # True

print(a < d)    # False
print(a > d)    # True

