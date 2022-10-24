import mysql.connector

conDB=mysql.connector.connect(host="localhost", user="admin", password="password", database="aeropuertos")

cur = conDB.cursor()

with open("alumnos.sql") as f:
    sql = f.read()

resultados=cur.execute(sql, multi=True)
# try:
#     for r in resultados:
#         print(r)
#
# except Exception as e:
#     print("FIN")

sql="create table alumnos3(id int(11))"
resultados=cur.execute(sql)

