import sqlite3
con = sqlite3.connect('card.s3db')
cursor = con.cursor()
a = cursor.execute('select balance from card where number = %s' % )
print(a)
for i in a:
    print(i)