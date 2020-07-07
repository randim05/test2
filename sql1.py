import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('DROP TABLE card')
conn.commit()
cur.execute('''CREATE TABLE card (    
            id INTEGER,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0)''')   #IF NOT EXISTS
conn.commit()
print(cur.fetchall())
id = 7
temp_card_number = "123"
pin = "1"
balance = 0
cur.execute("INSERT INTO card VALUES (%d, %s, %s, %d)"
            % (id, temp_card_number, pin, balance))
conn.commit()
print(cur.fetchall())
a = cur.execute('select * from card')
for i in a:
    print(i)