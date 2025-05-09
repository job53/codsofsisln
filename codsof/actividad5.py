import sqlite3

db_file = './testing.db'
con = sqlite3.connect(db_file)
cur = con.cursor()

cur.execute("select * from materias")
table_list = cur.fetchall()
for row in table_list:
        print(row)
con.close()