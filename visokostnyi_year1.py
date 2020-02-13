a=int(input())
print(a%4==0)
print(a%100==0)
print(a%400==0)

if a%4!=0:
    print("Обычный")
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("Високостный")
    if a%100==0:
        if a % 400!= 0:
            print("Обычный")
    if a%100!=0:
        if a%400!=0:
            print("Високостный")

