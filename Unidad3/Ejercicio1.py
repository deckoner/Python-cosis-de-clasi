from OlimpiadasBD import *
from Unidad3.OlimpiadasSQLlite import *
import csv
import os


def buscarEventoxOlimpiada(eventos, olimpiadaID, eventoNombre):
    for evento in eventos:
        if evento[0] == eventoNombre and evento[1] == olimpiadaID:
            return True, evento[2]

    return False, 0

def crearBaseDatos():
    crearEstructuraBaseDatos()
    vaciarInfoScript()

    rutaDelArchivo = input("Introduce la ruta del archivo CSV")

    if (os.path.exists(rutaDelArchivo) == True):
        if cargarDatos(rutaDelArchivo) == True:
            print("La base de datos ha sido creada y los datos cargados")

        else:
            vaciarInfoScript()
            print("Ha ocurrido un error en la carga")

    else:
        print("El archivo CSV no existe")


def crearBaseDatosLite():
    crearEstructuraBaseDatosLite()

    rutaDelArchivo = input("Introduce la ruta del archivo CSV")

    if (os.path.exists(rutaDelArchivo) == True):
        if cargarDatosLite(rutaDelArchivo) == True:
            print("La base de datos ha sido creada y los datos cargados")

        else:
            vaciarBaseDatosLite()
            print("Ha ocurrido un error en la carga")

    else:
        print("El archivo CSV no existe")

def cargarDatos(rutaDelArchivo):
    try:
        # Generamos los diccionarios
        equipo = {}
        deporte = {}
        deportista = {}
        Olimpiada = {}
        eventos = []

        # IDs de tablas
        deporteID = 0
        equipoID = 0
        deportistaID = 0
        olimpiadaID = 0
        eventoID = 0

        with open(rutaDelArchivo) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:

                    if not row["Team"] in equipo:
                        equipoID += 1
                        equipo[row["Team"]] = equipoID
                        rellenarEquipo(str(equipoID),row["Team"], row["NOC"])

                    if not row["Sport"] in deporte:
                        deporteID += 1
                        deporte[row["Sport"]] = deporteID
                        rellenarDeporte(str(deporteID), row["Sport"])

                    if not row["Name"] in deportista:
                        deportistaID += 1
                        deportista[row["Name"]] = deportistaID

                        # Comprobamos que la altura tenga valor si no tiene lo ponemos a cero ya que el campo de la
                        # Base de datos es Integer
                        if row["Weight"] == "NA":
                            peso = 0;
                        else:
                            peso = row["Weight"]

                        if row["Height"] == "NA":
                            altura = 0;
                        else:
                            altura = row["Height"]
                        rellenarDeportista(str(deportistaID), row["Name"], row["Sex"], str(peso), str(altura))

                    if not row["Games"] in Olimpiada:
                        olimpiadaID += 1
                        Olimpiada[row["Games"]] = olimpiadaID
                        rellenarOlimpiada(str(olimpiadaID), row["Games"], row["Year"], row["Season"], row["City"])

                    eventoRelacion = buscarEventoxOlimpiada(eventos, Olimpiada[row["Games"]], row["Event"])

                    if not eventoRelacion[0]:
                        eventoID += 1
                        eventos.append([row["Event"], Olimpiada[row["Games"]], eventoID])
                        rellenarEvento(str(eventoID), str(row["Event"]), str(Olimpiada[row["Games"]]), str(deporte[row["Sport"]]))

                    eventoRelacion = buscarEventoxOlimpiada(eventos, Olimpiada[row["Games"]], row["Event"])

                    rellenarParticipacion(str(deportista[row["Name"]]), str(eventoRelacion[1]), str(equipo[row["Team"]]), str(row["Age"]), str(row["Medal"]))
        return True

    except:
        return False


def cargarDatosLite(rutaDelArchivo):
    try:
        # Generamos los diccionarios
        equipo = {}
        deporte = {}
        deportista = {}
        Olimpiada = {}
        evento = {}

        # IDs de tablas
        deporteID = 0
        equipoID = 0
        deportistaID = 0
        olimpiadaID = 0
        eventoID = 0

        with open(rutaDelArchivo) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:

                if not row["Team"] in equipo:
                    equipoID += 1
                    equipo[row["Team"]] = equipoID
                    rellenarEquipoLite(str(equipoID), row["Team"], row["NOC"])

                if not row["Sport"] in deporte:
                    deporteID += 1
                    deporte[row["Sport"]] = deporteID
                    rellenarDeporteLite(str(deporteID), row["Sport"])

                if not row["Name"] in deporte:
                    deportistaID += 1
                    deportista[row["Name"]] = deportistaID

                    # Comprobamos que la altura tenga valor si no tiene lo ponemos a cero ya que el campo de la
                    # Base de datos es Integer
                    if row["Weight"] == "NA":
                        peso = 0;
                    else:
                        peso = row["Weight"]

                    if row["Height"] == "NA":
                        altura = 0;
                    else:
                        altura = row["Height"]

                    rellenarDeportistaLite(str(deportistaID), row["Name"], row["Sex"], str(peso), str(altura))

                if not row["Games"] in deporte:
                    olimpiadaID += 1
                    Olimpiada[row["Games"]] = olimpiadaID
                    rellenarOlimpiadaLite(str(olimpiadaID), row["Games"], row["Year"], row["Season"], row["City"])

                if not row["Event"] in evento:
                    eventoID += 1
                    evento[row["Event"]] = eventoID

                    rellenarEventoLite(str(eventoID), str(row["Event"]), str(Olimpiada[row["Games"]]),
                                   str(deporte[row["Sport"]]))

                rellenarParticipacionLite(str(deportista[row["Name"]]), str(evento[row["Event"]]), str(equipo[row["Team"]]),
                                      str(row["Age"]), str(row["Medal"]))

        return True

    except:
        return False


def SelecionarSQL():

    while True:
        print("""
        0. Base MySQL
        1. Base SQLLite
        """)
        sql = input("Elija una de las dos opciones con un numero")

        if (sql == "0" ):
            return True

        if (sql == "1"):
            return False

        print("Porfavor introduzca una opcion valida")


# Esta funcion sera usada para selecionar la id de un elemento des de una consulta SQL
def selecionPorID(listaElementos, posicionCampoMostrar, txt):

    nElemento = 0
    # Mostraremos todos los elementos de la lista junto con un ID para su selecion
    for e in listaElementos:
        print(str(nElemento) + "- " + txt + ": " + e[posicionCampoMostrar])
        nElemento += 1

    # Le pedimos al usuario que elija una de las IDs, le metemos en un bucle hasta que selecione alguna correcta
    while True:
        eleccion = int(input("Elija la edicion olimpica usando la ID porfavor"))

        if (eleccion <= len(listaElementos)):
            idYNombre = listaElementos[eleccion]

            break

    # Devolvemos la id
    return idYNombre


def listarDeportistaEvento():
    # Preguntamos al usuario si va a usar SQL (True) o SQLLite (False)
    SQL = SelecionarSQL()

    # Primero hacemos que el usuario elija la temporada
    while True:
        eleccion = input("elegir temporada: Summer (S) o Winter (W)").upper()

        if eleccion == "S":
            temporada = "Summer"
            break

        if eleccion == "W":
            temporada = "Winter"
            break

    # Usaremos la selecionarPorID para coger las diferentes ID que necesitamos del usuario
    if (SQL):
        idOlimpiadaNombre = selecionPorID(listarOlimpiadasXTemporada(temporada), 1, "Nombre Olimpiada")
    else:
        idOlimpiadaNombre = selecionPorID(listarOlimpiadasXTemporadaLite(temporada), 1, "Nombre Olimpiada")

    if (SQL):
        idDeporteNombre = selecionPorID(listarDeporteXOlimpiada(idOlimpiadaNombre[0]), 1, "Nombre deporte")
    else:
        idDeporteNombre = selecionPorID(listarDeporteXOlimpiadaLite(idOlimpiadaNombre[0]), 1, "Nombre deporte")

    if (SQL):
        idEventoNombre = selecionPorID(listarEventosXOlimpiadaXDeporte(idOlimpiadaNombre[0], idDeporteNombre[0]), 1,
                                       "Nombre evento")
    else:
        idEventoNombre = selecionPorID(listarEventosXOlimpiadaXDeporteLite(idOlimpiadaNombre[0], idDeporteNombre[0]), 1,
                                       "Nombre evento")

    if (SQL):
        listaParticipantes = listarDeportistasEvento(idEventoNombre[0])
    else:
        listaParticipantes = listarDeportistasEventoLite(idEventoNombre[0])

    for p in listaParticipantes:
        print("""
        Nombre: %s
        Edad: %s
        Altura: %s
        Peso: %s
        Equipo: %s
        Medalla ganada: %s""" % (p[0], p[3], p[1], p[2], p[5], p[4]))


def modificarMedalla():
    # Preguntamos al usuario si va a usar SQL (True) o SQLLite (False)
    SQL = SelecionarSQL()


def menu():
    finalizar = True

    while finalizar == True:
        print("""
        1.Crear BBDD MySQL
        2.Crear BBDD SQLite
        3.Listado de deportistas en diferentes deportes
        4.Listado de deportistas participantes
        5.Modificar medalla deportista
        6.Añadir deportista/participación
        7.Eliminar participación


        0.Salir
        """)

        opcion = int(input("Porfavor elige una opcion escribiendo un numero"))

        if opcion == 1:
            crearBaseDatos()

        if opcion == 2:
            crearBaseDatosLite()

        if opcion == 3:
            pass

        if opcion == 4:
            listarDeportistaEvento()

        if opcion == 5:
            pass

        if opcion == 6:
            pass

        if opcion == 7:
            pass

        if opcion == 0:
            finalizar = False


if __name__ == '__main__':
    vaciarInfoScript()
    if cargarDatos("/home/dm2/repo/Python/Unidad3/athlete_eventsChiquito.csv"):
        print("No pete")
    else:
        print("Si pete")

    pass