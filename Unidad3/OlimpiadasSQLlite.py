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


def listarOlimpiadasXTemporadaLite(temporada):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = "SELECT * FROM Olimpiada WHERE temporada = ?;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (temporada,))

    olimpiadas = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close

    return olimpiadas


def listarDeporteXOlimpiadaLite(idOlimpiada):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = "SELECT Evento.id_deporte, Deporte.nombre FROM Evento, Deporte " \
                "WHERE Evento.id_olimpiada = ? AND Evento.id_deporte = Deporte.id_deporte;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (idOlimpiada,))

    deportes = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close

    return deportes


def listarEventosXOlimpiadaXDeporteLite(idOlimpiada, idDeporte):
    # Creamos la conecxion a la base de datos y el cursor
    con = _abrirConecxion()
    cur = con.cursor()

    sentencia = "SELECT Evento.id_evento, Evento.nombre FROM Evento WHERE Evento.id_deporte = ? " \
                "AND Evento.id_olimpiada = ?;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (idDeporte, idOlimpiada))

    eventos = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    con.close

    return eventos


def listarDeportistasEventoLite(idEvento):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT DISTINCT Deportista.nombre, Deportista.altura, Deportista.peso, Participacion.edad, " \
                "Participacion.medalla, Equipo.nombre FROM Deportista, Participacion, " \
                "Equipo WHERE Participacion.id_evento = ? " \
                "AND Participacion.id_deportista = Deportista.id_deportista " \
                "AND Participacion.id_equipo = Equipo.id_equipo;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (idEvento,))

    participantes = cur.fetchall()

    return participantes