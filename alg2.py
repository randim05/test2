# import collections.abc
def foo(numbers):
    counter1 = 0
    counter2 = 0

    for num in numbers:
        if num % 2 == 0:
            counter1 += num if num < 4 else -num
        else:
            counter2 += num if num < 5 else -num

    return counter1 * counter2

print(foo([3, 4, 2, 1, 5, 7]))