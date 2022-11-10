import sqlite3

con = sqlite3.connect("enbebido.db")
cur = con.cursor()

with open ("olimpiadas.db.sql") as f:
    cur.executescript(f.read())

sql1 = "insert into Equipo values (12, 'Malasia', 'MLS')"
sql2 = "insert into Equipo values (13, 'Argentina', 'ARG')"

cur.execute(sql1)
cur.execute(sql2)

consulta = "select id_equipo from Equipo"
resultado = cur.execute(consulta)
for r in resultado:
    print(r)