import mysql.connector


def _abrirConecxion():
    # Crear conector a la base de datos
    conDB=mysql.connector.connect(host="localhost", user="admin", password="password", database="olimpiadaspy")

    return conDB


def crearEstructuraBaseDatos():
    # Creamos la conecxion a la base de datos sin elegir schema y el cursor
    conDB = mysql.connector.connect(host="localhost", user="admin", password="password")
    cur = conDB.cursor()

    # Cargar setencias sql
    with open("olimpiadas.sql") as f:
        sql = f.read()

    resultados = cur.execute(sql, multi=True)

    try:
        # Ejecutar setencias sql
        for r in resultados:
            pass

    except Exception as e:
        pass

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def vaciarInfoScript():
    # Abrimos la conecxion y creamos un cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    vaciarEquipo = "DELETE FROM Equipo;"
    vaciarDeporte = "DELETE FROM Deporte;"
    vaciarDeportista = "DELETE FROM Deportista;"
    vaciarOlimpiada = "DELETE FROM Olimpiada;"
    vaciarEvento = "DELETE FROM Evento"
    vaciarParticipacion = "DELETE FROM Participacion"

    # Ejecutamos las consultas en orden para evitar errore en la base de datos
    cur.execute(vaciarParticipacion)
    cur.execute(vaciarEvento)
    cur.execute(vaciarEquipo)
    cur.execute(vaciarDeporte)
    cur.execute(vaciarDeportista)
    cur.execute(vaciarOlimpiada)

    # Hacemos el comit para guardar los cambios en la base de datos
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


# Metodos para rellenar la base de datos
def rellenarEquipo(idEquipo, pais, iniciales):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "INSERT INTO `olimpiadaspy`.`Equipo` (`id_equipo`, `nombre`, `iniciales`) VALUES ('"+idEquipo+"', '"+pais+"', '"+iniciales+"');"

    cur.execute(sentencia)
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def rellenarDeporte(idDeporte, deporte):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "INSERT INTO `olimpiadaspy`.`Deporte` (`id_deporte`, `nombre`) VALUES ('" + idDeporte + "', '" + deporte + "');"

    cur.execute(sentencia)
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def rellenarDeportista(id, nombre, genero, peso, altura):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "INSERT INTO `olimpiadaspy`.`Deportista` (`id_deportista`, `nombre`, `sexo`, `peso`, `altura`) VALUES " \
               "('"+id+"', '"+nombre+"', '"+genero+"', '"+peso+"', '"+altura+"'); "

    cur.execute(sentencia)
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def rellenarEvento(idEvento, nombre, idOlimpiada, iddeporte):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia ="INSERT INTO `olimpiadaspy`.`Evento` (`id_evento`, `nombre`, `id_olimpiada`, `id_deporte`) VALUES (%s, %s, %s, %s);"

    cur.execute(sentencia, (idEvento, nombre, idOlimpiada, iddeporte))
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def rellenarOlimpiada(idOlimpiada, nombre, anio, temporada, ciudad):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "INSERT INTO `olimpiadaspy`.`Olimpiada` (`id_olimpiada`, `nombre`, `anio`, `temporada`, `ciudad`) VALUES" \
    "('"+idOlimpiada+"', '"+nombre+"', '"+anio+"', '"+temporada+"', '"+ciudad+"');"

    cur.execute(sentencia)
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def rellenarParticipacion(idDeportista, idEvento, idEquipo, edad, medalla):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "INSERT INTO `olimpiadaspy`.`Participacion` (`id_deportista`, `id_evento`, `id_equipo`, `edad`, " \
                "`medalla`) VALUES ( %s, %s, %s, %s, %s);"

    cur.execute(sentencia, (idDeportista, idEvento, idEquipo, edad, medalla))
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def listarOlimpiadasXTemporada(temporada):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT * FROM olimpiadaspy.Olimpiada WHERE temporada = %s;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (temporada,))

    olimpiadas = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return olimpiadas


def listarDeporteXOlimpiada(idOlimpiada):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT Evento.id_deporte, Deporte.nombre FROM olimpiadaspy.Evento, olimpiadaspy.Deporte " \
                "WHERE Evento.id_olimpiada = %s AND Evento.id_deporte = Deporte.id_deporte;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (idOlimpiada,))

    deportes = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return deportes


def listarEventosXOlimpiadaXDeporte(idOlimpiada, idDeporte):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT Evento.id_evento, Evento.nombre FROM olimpiadaspy.Evento WHERE Evento.id_deporte = %s " \
                "AND Evento.id_olimpiada = %s;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (idDeporte, idOlimpiada))

    eventos = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return eventos


def listarDeportistasEvento(idEvento):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT DISTINCT Deportista.nombre, Deportista.altura, Deportista.peso, Participacion.edad, " \
                "Participacion.medalla, Equipo.nombre FROM olimpiadaspy.Deportista, olimpiadaspy.Participacion, " \
                "olimpiadaspy.Equipo WHERE Participacion.id_evento = %s " \
                "AND Participacion.id_deportista = Deportista.id_deportista " \
                "AND Participacion.id_equipo = Equipo.id_equipo;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (idEvento,))

    participantes = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return participantes


def listarDeportistas():
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT id_deportista, nombre FROM olimpiadaspy.Deportista;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia)

    deportistas = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return deportistas


def listarDeportistaIDDeportista(idDeportista):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT Evento.id_evento, Evento.nombre, Participacion.medalla FROM olimpiadaspy.Participacion, " \
                "olimpiadaspy.Evento WHERE Participacion.id_evento = Evento.id_evento AND id_deportista = %s;"

    cur.execute(sentencia, (idDeportista,))

    eventos = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return eventos


def modificarMedalla(idDeportista, idEvento, medalla):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "UPDATE Participacion SET medalla = "+medalla+" WHERE (id_deportista = "+idDeportista+") " \
                "AND (id_evento = "+idEvento+");"

    cur.execute(sentencia)
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def eliminarParticipacion(idDeportista, idEvento):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "DELETE FROM `olimpiadaspy`.`Participacion` WHERE (`id_deportista` = %s) AND (`id_evento` = %s);"

    cur.execute(sentencia, (idDeportista, idEvento))
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def eliminarDeportista(idDeportista):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "DELETE FROM `olimpiadaspy`.`Deportista` WHERE (`id_deportista` = %s);"

    cur.execute(sentencia, (idDeportista,))
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

def crearDeportistaUsuario(nombre, genero, peso, altura):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "INSERT INTO `olimpiadaspy`.`Deportista` (`nombre`, `sexo`, `peso`, `altura`) " \
                "VALUES (%s, %s, %s, %s);"

    cur.execute(sentencia, (nombre, genero, peso, altura))
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

def listarEquipos():
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT * FROM olimpiadaspy.Equipo;"

    cur.execute(sentencia)

    equipos = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return equipos


def crearParticipacion(idDeportista, idEvento, idEquipo, edad, medalla):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "INSERT INTO `olimpiadaspy`.`Participacion` (`id_deportista`, `id_evento`, `id_equipo`, " \
                "`edad`, `medalla`) VALUES (%s, %s, %s, %s, %s);"

    cur.execute(sentencia, (idDeportista, idEvento, idEquipo, edad, medalla))
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close
