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
# import dis
# def a():
#     try:
#         print('try')
#         raise Exception
#     except:
#         return 1
#         pass
#     else:
#         return 2
#     finally:
#         print('finally')
#
# print(dis.Bytecode(a))


#
# text = input()
# # text = text.lower()
# print(text)
# words = text.split()
# print(words)
# for word in words:
#     if word.startswith(("https:", "http:", 'www.', "WWW.")):
#         print(word)


print(14/3)
print(14//3)
# print(14/3)