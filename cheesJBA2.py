col = int(input())
row = int(input())
print((col == 1 or col == 8) and (row == 1 or row == 8))
print((col != 1 or col != 8) and (row != 1 or row != 8))
if (col == 1 or col == 8) and (row == 1 or row == 8):
    print("3")
elif (col != 1 or col != 8) and (row != 1 or row != 8):
    print("8")
else:
    print("5")
