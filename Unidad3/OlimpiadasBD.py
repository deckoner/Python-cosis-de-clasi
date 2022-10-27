import mysql.connector


def abrirConecxion():
    # Crear conector a la base de datos
    conDB=mysql.connector.connect(host="localhost", user="admin", password="password", database="olimpiadaspy")

    return conDB


def crearEstructuraBaseDatos():
    # Crear cursir a la base de datos
    cur = abrirConecxion()

    # Cargar setencias sql
    with open("olimpiadas.sql") as f:
        sql = f.read()
    resultados=cur.execute(sql, multi=True)

    # Ejecutar setencias sql
    try:
        for r in resultados:
            print(r)

    except Exception as e:
        print("FIN")

def rellenarEquipo(pais, iniciales):

    # Creamos la conecxion a la base de datos y el cursor
    conDB = abrirConecxion()
    cur = conDB.cursor()

    setencia = "INSERT INTO `olimpiadaspy`.`Equipo` (`nombre`, `iniciales`) VALUES ('"+pais+"', '"+iniciales+"');"

    cur.execute(setencia)
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

def rellenarDeporte(deporte):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = abrirConecxion()
    cur = conDB.cursor()

    setencia = "INSERT INTO `olimpiadaspy`.`Deporte` (`nombre`) VALUES ('"+deporte+"');"

    cur.execute(setencia)
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def rellenarDeportista(id, nombre, genero, peso, altura):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = abrirConecxion()
    cur = conDB.cursor()

    setencia = "INSERT INTO `olimpiadaspy`.`Deportista` (`id_deportista`, `nombre`, `sexo`, `peso`, `altura`) VALUES " \
               "('"+id+"', '"+nombre+"', '"+genero+"', '"+peso+"', '"+altura+"'); "

    cur.execute(setencia)
    conDB.commit()


def rellenarEvento(idEvento, nombre, idOlimpiada, iddeporte):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = abrirConecxion()
    cur = conDB.cursor()

    setencia = "INSERT INTO `olimpiadaspy`.`Evento` (`id_evento`, `nombre`, `id_olimpiada`, `id_deporte`) VALUES ('" \
               +idEvento+"', '"+nombre+"', '"+idOlimpiada+"', '"+iddeporte+"');"

    cur.execute(setencia)
    conDB.commit()


def rellenarOlimpiada(idOlimpiada, nombre, anio, temporada, ciudad):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = abrirConecxion()
    cur = conDB.cursor()

    setencia = "INSERT INTO `olimpiadaspy`.`Olimpiada` (`id_olimpiada`, `nombre`, `anio`, `temporada`, `ciudad`) VALUES" \
    "('"+idOlimpiada+"', '"+nombre+"', '"+anio+"', '"+temporada+"', '"+ciudad+"');"

    cur.execute(setencia)
    conDB.commit()


def rellenarParticipacion():

    sentencia = "INSERT INTO `olimpiadaspy`.`Participacion` (`id_deportista`, `id_evento`, `id_equipo`, `edad`, " \
                "`medalla`) VALUES ('2321', '123', '123', '123', 'joro'); "