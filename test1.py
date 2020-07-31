# def shift_inplace(lst, k):
#     size = len(lst)
#     lst[k:], lst[0:k] = lst[0:-k], lst[-k:]
#
#
# lst = list(range(10))
#
# shift_inplace(lst, -3)
# print(lst)
#
# shift_inplace(lst, 5)
# print(lst)
#
import dis
def a():
    try:
        print('try')
        raise Exception
    except:
        return 1
        pass
    else:
        return 2
    finally:
        print('finally')

print(dis.Bytecode(a))