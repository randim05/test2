def shift_inplace(lst, k):
    size = len(lst)
    lst[k:], lst[0:k] = lst[0:-k], lst[-k:]


lst = list(range(10))

shift_inplace(lst, -3)
print(lst)

shift_inplace(lst, 5)
print(lst)

