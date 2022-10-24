import mysql.connector


conDB=mysql.connector.connect(host="localhost", user="admin", password="password")

cur = conDB.cursor()

with open("alumnos.sql") as f:
    sql = f.read()