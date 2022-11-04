import sqlite3

def _abrirConecxion():
    # Crear conector a la base de datos
    conDB = sqlite3.connector.connect(host="localhost", user="admin", password="password", database="olimpiadaspy")

    return conDB


def crearEstructuraBaseDatos():
    # Creamos la conecxion a la base de datos sin elegir schema y el cursor
    conDB = sqlite3.connect("olimpiadas.db")

    # Cargar setencias sql
    with open("olimpiadasLite.sql") as f:
        sql = f.read()

    resultados = conDB.execute(sql)

    try:
        # Ejecutar setencias sql
            pass

    except:
        pass


if __name__ == '__main__':
    crearEstructuraBaseDatos()