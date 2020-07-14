import sqlite3
conn = sqlite3.connect('card.s3db')  # cards saves here) card_number : CreditCard
cur = conn.cursor()
cn = "4000007999221589"
h = cur.execute("select * from card where number = %s" % cn).fetchone()[0]
print(h)
