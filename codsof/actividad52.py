import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()
con = sqlite3.connect(dataBaseManager.database)

materia = (11,"t","joey",100)
dataBaseManager.create_materia(con,materia)

cur = con.cursor()

cur.execute("select * from materias")
table_list = cur.fetchall()
for row in table_list:
        print(row)
con.close()