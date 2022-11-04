from OlimpiadasBD import *
import csv
import os


def crearBaseDatos():
    crearEstructuraBaseDatos()

    rutaDelArchivo = input("Introduce la ruta del archivo CSV")

    if (os.path.exists(rutaDelArchivo) == True):
        if cargarDatos(rutaDelArchivo) == True:
            print("La base de datos ha sido creada y los datos cargados")

        else:
            # Volvemos a crear la estructura ya que esto dejara la base da datos limpia
            crearEstructuraBaseDatos()
            print("Ha ocurrido un error en la carga")

    else:
        print("El archivo CSV no existe")


def cargarDatos():
    # Generamos los diccionarios
    equipos = {}
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

    with open("athlete_eventsChiquito.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        reader.remove(0)

        for row in reader:
                print(row["Event"])

                if not row["Team"] in equipos:
                    equipoID += 1
                    equipos[row["Team"]] = equipoID
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

                    rellenarDeportista(str(deportistaID), row["Name"], row["Sex"], peso, altura)

                if not row["Games"] in deporte:
                    olimpiadaID += 1
                    Olimpiada[row["Games"]] = olimpiadaID
                    rellenarOlimpiada(str(olimpiadaID), row["Games"], row["Year"], row["Season"], row["City"])

                if not row["Event"] in evento:
                    eventoID += 1
                    evento[row["Event"]] = eventoID

                    print(row["Games"])
                    print(row["Event"])
                    print(row["Medal"])

                    # Limpiamos las comillas simples del nombre del evento
                    nombreEvento = row["Event"].replace("'", " ")

                    print(nombreEvento)

                    rellenarEvento(str(eventoID), nombreEvento, str(Olimpiada[row["Games"]]), str(deporte[row["Sport"]]))

                rellenarParticipacion(str(deportista[row["Name"]]), str(evento[row["Event"]]), str(deporte[row["Sport"]]), row["Age"], row["Medal"])

        return True


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
            pass

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
    crearEstructuraBaseDatos()
    cargarDatos()