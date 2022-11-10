from OlimpiadasBD import *
from Unidad3.OlimpiadasSQLlite import *
import csv
import os


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
                        rellenarEquipo(str(equipoID),row["Team"], row["NOC"])

                    if not row["Sport"] in deporte:
                        deporteID += 1
                        deporte[row["Sport"]] = deporteID
                        rellenarDeporte(str(deporteID), row["Sport"])

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

                        rellenarDeportista(str(deportistaID), row["Name"], row["Sex"], str(peso), str(altura))

                    if not row["Games"] in deporte:
                        olimpiadaID += 1
                        Olimpiada[row["Games"]] = olimpiadaID
                        rellenarOlimpiada(str(olimpiadaID), row["Games"], row["Year"], row["Season"], row["City"])

                    if not row["Event"] in evento:
                        eventoID += 1
                        evento[row["Event"]] = eventoID

                        rellenarEvento(str(eventoID), str(row["Event"]), str(Olimpiada[row["Games"]]), str(deporte[row["Sport"]]))

                    rellenarParticipacion(str(deportista[row["Name"]]), str(evento[row["Event"]]), str(equipo[row["Team"]]), str(row["Age"]), str(row["Medal"]))

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
        1. Base MySQL
        2. Base SQLLite
        """)
        sql = input("Elija una de las dos opciones con un numero")

        if (sql == "1" ):
            return True

        if (sql == "2"):
            return False

        print("Porfavor introduzca una opcion valida")


def listarDeportistaEvento():
    if (SelecionarSQL):

        # Primero hacemos que el usuario elija la temporada
        while True:
            eleccion = input("elegir temporada: Summer (S) o Winter (W)").upper()

            if eleccion == "S":
                summer = True
                break

            if eleccion == "W":
                summer = False
                break

        listaOlimpiadas = mostrarOlimpiadas(summer)

        for e in listaOlimpiadas:
            print(e[0] + "- " + e[1])

        eleccion = input("Elija la edicion olimpica usando la ID porfavor")

        while True:
            if (eleccion >= len(listaOlimpiadas)):
                idOlimpiada = eleccion

    else:
        pass


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
            pass

        if opcion == 5:
            pass

        if opcion == 6:
            pass

        if opcion == 7:
            pass

        if opcion == 0:
            finalizar = False


if __name__ == '__main__':
    crearBaseDatosLite()
    pass