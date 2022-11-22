import mysql.connector


def _abrirConecxion():
    # Crear conector a la base de datos
    conDB=mysql.connector.connect(host="172.20.132.130", user="ex2", password="adat", database="examen2")

    return conDB

def notaDeAlumnos():
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia ="SELECT alumnos.APENOM, asignaturas.ABREVIATURA, notas.NOTA FROM examen2.alumnos, examen2.asignaturas, " \
               "examen2.notas WHERE alumnos.DNI = notas.DNI AND notas.COD = asignaturas.COD GROUP BY alumnos.APENOM desc;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia)

    ListaAlumnos = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return ListaAlumnos


def existeNombreAlumno(dni):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT APENOM FROM examen2.alumnos WHERE DNI = %s;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (dni,))

    try:
        nombre = cur.next()

        # Cerramos el cursor y la base de datos
        cur.close()
        conDB.close

        return True
    except:
        return False


def mostrarNombreAlumno(dni):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT APENOM FROM examen2.alumnos WHERE DNI = %s;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (dni,))

    nombre = cur.next()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return nombre


def cambiarNombre(dni, nombre):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "UPDATE examen2.alumnos SET APENOM = %s WHERE (DNI = %s);"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (nombre, dni))

    # Hacemos el comit
    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def listarAsignaturas():
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT * FROM examen2.asignaturas;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia)

    lista = cur.fetchall()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close

    return lista


def existeClasificacion(codigo, dni):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "SELECT notas.NOTA FROM examen2.alumnos, examen2.notas WHERE COD = %s AND alumnos.DNI = notas.DNI " \
                "AND alumnos.DNI = %s;"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (codigo, dni))

    try:
        cur.next()

        # Cerramos el cursor y la base de datos
        cur.close()
        conDB.close

        return True
    except:
        return False



def actualizarNota(nota, codigo, dni):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "UPDATE `examen2`.`notas` SET `NOTA` = %s WHERE (`DNI` = %s) and (`COD` = %s);"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (nota, dni, codigo))

    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close


def crearNota(dni, codigo, nota):
    # Creamos la conecxion a la base de datos y el cursor
    conDB = _abrirConecxion()
    cur = conDB.cursor()

    sentencia = "INSERT INTO `examen2`.`notas` (`DNI`, `COD`, `NOTA`) VALUES (%s, %s, %s);"

    # Ejecutamos la conmsulta
    cur.execute(sentencia, (dni, codigo, nota))

    conDB.commit()

    # Cerramos el cursor y la base de datos
    cur.close()
    conDB.close