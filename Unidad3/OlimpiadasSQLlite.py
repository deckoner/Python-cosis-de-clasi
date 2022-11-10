import sqlite3

def _abrirConecxion():
    con = sqlite3.connect("enbebido.db")

    return con


def crearEstructuraBaseDatosLite():

    try:
        con = _abrirConecxion()
        cur = con.cursor()

        with open("olimpiadas.db.sql") as f:
            cur.executescript(f.read())

        cur.close()
        con.close()

        return True

    except:
        return False


def vaciarBaseDatosLite():
    # Abrimos una conecxion a la base de datos y creamos un cursor
    con = _abrirConecxion()
    cur = con.cursor()

    vaciarEquipo = "DELETE FROM Equipo;"
    vaciarDeporte = "DELETE FROM Deporte;"
    vaciarDeportista = "DELETE FROM Deportista;"
    vaciarOlimpiada = "DELETE FROM Olimpiada;"
    vaciarEvento = "DELETE FROM Evento"
    vaciarParticipacion = "DELETE FROM Participacion"

    # Ejecutamos las consultas en orden para evitar errore en la base de datos
    cur.execute(vaciarParticipacion)
    cur.execute(vaciarEvento)
    cur.execute(vaciarOlimpiada)
    cur.execute(vaciarDeportista)
    cur.execute(vaciarDeporte)
    cur.execute(vaciarEquipo)

    # Hacemos un comit para guardar los cambios
    con.commit()

    # Cerramos el cursor y la conecxion a la base de datos
    cur.close()
    con.close()


# Metodos para rellenar la base de datos
def rellenarEquipoLite(idEquipo, pais, iniciales):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = 'INSERT INTO "main"."Equipo"("id_equipo", "nombre", "iniciales") VALUES (?, ?, ?);'

    # Ejecutamos la consulta y hacemos el comit
    cur.execute(sentencia, (idEquipo, pais, iniciales))
    con.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close


def rellenarDeporteLite(idDeporte, deporte):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = 'INSERT INTO "main"."Deporte"("id_deporte", "nombre") VALUES (?, ?);'

    cur.execute(sentencia, (idDeporte, deporte))
    con.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close


def rellenarDeportistaLite(id, nombre, genero, peso, altura):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = 'INSERT INTO "main"."Deportista"("id_deportista", "nombre", "sexo", "peso", "altura") ' \
                'VALUES (?, ?, ?, ?, ?);'

    cur.execute(sentencia, (id, nombre, genero, peso, altura))
    con.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close


def rellenarEventoLite(idEvento, nombre, idOlimpiada, iddeporte):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = 'INSERT INTO "main"."Evento"("id_evento", "nombre", "id_olimpiada", "id_deporte") VALUES (?, ?, ?, ?);'

    cur.execute(sentencia, (idEvento, nombre, idOlimpiada, iddeporte))
    con.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close


def rellenarOlimpiadaLite(idOlimpiada, nombre, anio, temporada, ciudad):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = 'INSERT INTO "main"."Olimpiada"("id_olimpiada", "nombre", "anio", "temporada", "ciudad") ' \
                'VALUES (?, ?, ?, ?, ?);'

    cur.execute(sentencia, (idOlimpiada, nombre, anio, temporada, ciudad))
    con.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close


def rellenarParticipacionLite(idDeportista, idEvento, idEquipo, edad, medalla):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = 'INSERT INTO "main"."Participacion"("id_deportista", "id_evento", "id_equipo", "edad", "medalla") ' \
                'VALUES (?, ?, ?, ?, ?);'

    cur.execute(sentencia, (idDeportista, idEvento, idEquipo, edad, medalla))
    con.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close