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

    except:
        pass


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

    sentencia ="INSERT INTO `olimpiadaspy`.`Evento` (`id_evento`, `nombre`, `id_olimpiada`, `id_deporte`) VALUES ('%s', '%s', '%s', '%s');"

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
                "`medalla`) VALUES ('" +idDeportista+ "', '" +idEvento+ "', '" +idEquipo+ "', '" +edad+ "', '"+medalla+"');"

    cur.execute(sentencia)
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close