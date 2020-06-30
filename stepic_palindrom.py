# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])

s=input()
set_s=set(s)
res = {}
for i in s:
    for j in set_s:
        if i == j:
            if i not in res.keys():
                res[i] = 1
            else:
                res[i] += 1
res_k=sorted(res)
out=[]
for i in res_k:
    out.append(i)
    out.append(res[i])
#
for i in out:
    i = str(i)
print(out)
print(''.join(out))
