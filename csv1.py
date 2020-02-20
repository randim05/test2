import csv, os
files = os.listdir(".")
for i in files:
    with open(i, 'w') as csvfile:
