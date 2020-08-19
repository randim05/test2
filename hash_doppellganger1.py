# the object_list has already been defined
# write your code here
from collections.abc import Hashable
temp = []

#working var
for i in object_list:
    if isinstance(i, Hashable):
        temp.append(i)
s = {}
for i in temp:
    if hash(i) not in s:
        s[hash(i)] = 1
    else:
        s[hash(i)] += 1

res = 0
for i in s:
    if s[i] != 1:
        res += s[i]

print(res)
#working var
hashmap()
#stert var
# in_list = len(object_list)
# out_list = len(set(temp))
# print(in_list - out_list)

# res = {}
# for i in temp:
#     if res == {}:
#         for j in temp[1:]:
#             if i is j:
#                 res[str(i)] = 1
#     else:
#         for j in temp[j+1:]:
#             if i not in res:
#                 res[str(i)] = 1
#             else:
#                 res[str(i)] += 1
# print(res)
# x = 0
# for i in res:
#     x += res[i]
# print(x)

#2var
# res = 1
# for i in temp:
#     if i in temp[i:]:
#         res += 1
#
# print(res)

#var 3
# res = 0
# x = 1
# for i in temp[x:]:
#     for j in temp[x:]:
#         if i is j:
#             res += 1
#     x += 1
# if res == 0:
#     print(res)
# else:
#     print(res + 1)