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
    listaDeportistas = listarDeportistas()

    nombre = input("Escribe el nombre o parte del nombre del deportista que quieras")

    listaDeportistasCopy = []

    for d in listaDeportistas:
        if nombre.lower() in d[1].lower():
            listaDeportistasCopy.append(d)

    if bool(listaDeportistasCopy):
        contadorDeportista = 0
        for d in listaDeportistasCopy:
            contadorDeportista +=1
            print(str(contadorDeportista) + "- " + d[1])

        # Bucle para que el usuario elija un deportista
        while True:
            try:
                eleccion = int(input("Porfavor elija un deportista de la lista usando el numero"))

                if eleccion <= len(listaDeportistasCopy):
                    break

            except:
                print("Debe de introducir un numero del 1 al " + str(contadorDeportista))

        listaEventos = listarDeportistaIDDeportista(listaDeportistasCopy[eleccion - 1][0])

        if bool(listaEventos):
            contadorEvento = 0
            for e in listaEventos:
                contadorEvento += 1
                print(str(contadorEvento) + "- " + e[1] + " Medalla: " + e[2])

            while True:
                try:
                    eleccionEvento = int(input("Porfavor elija un evento de la lista usando el numero"))

                    if eleccionEvento <= len(listaDeportistasCopy):
                        break

                except:
                    print("Debe de introducir un numero del 1 al " + str(contadorEvento))

            while True:
                try:
                    print("Elije por que medalla deseas cambiarlo")
                    print("1. Gold")
                    print("2. Silver")
                    print("3. bronze")
                    print("4. N/A")

                    eleccionMedalla = int(input("Porfavor elija un evento de la lista usando el numero"))

                    if eleccionMedalla == 1:
                        medalla = "Gold"
                        break

                    if eleccionMedalla == 2:
                        medalla = "Silver"
                        break

                    if eleccionMedalla == 3:
                        medalla = "bronze"
                        break

                    if eleccionMedalla == 4:
                        medalla = "N/A"
                        break

                except:
                    print("Elije una medalla mediante los numeros porfavor")

            modificarMedallaLite(listaDeportistasCopy[eleccion - 1][0], listaEventos[eleccionEvento - 1][0], medalla)
            modificarMedallaDB(listaDeportistasCopy[eleccion - 1][0], listaEventos[eleccionEvento - 1][0], medalla)

            print("Se ha actualizado correctamente la participacion")
        else:
            print("Este deportista no tiene participaciones")
    else:
        print("No se encontro ningun deportista que contenga ese nombre")


def eliminarParticipacion():
    listaDeportistas = listarDeportistas()

    nombre = input("Escribe el nombre o parte del nombre del deportista que quieras")

    listaDeportistasCopy = []

    for d in listaDeportistas:
        if nombre.lower() in d[1].lower():
            listaDeportistasCopy.append(d)

    if bool(listaDeportistasCopy):
        contadorDeportista = 0
        for d in listaDeportistasCopy:
            contadorDeportista +=1
            print(str(contadorDeportista) + "- " + d[1])

        # Bucle para que el usuario elija un deportista
        while True:
            try:
                eleccion = int(input("Porfavor elija un deportista de la lista usando el numero"))

                if eleccion <= len(listaDeportistasCopy):
                    break

            except:
                print("Debe de introducir un numero del 1 al " + str(contadorDeportista))

        listaEventos = listarDeportistaIDDeportista(listaDeportistasCopy[eleccion - 1][0])

        if bool(listaEventos):
            contadorEvento = 0
            for e in listaEventos:
                contadorEvento += 1
                print(str(contadorEvento) + "- " + e[1] + " Medalla: " + e[2])

            while True:
                try:
                    eleccionEvento = int(input("Porfavor elija un evento de la lista usando el numero"))

                    if eleccionEvento <= len(listaDeportistasCopy):
                        break

                except:
                    print("Debe de introducir un numero del 1 al " + str(contadorEvento))

            if len(listaEventos) == 1:
                eliminarParticipacionDB(listaDeportistasCopy[eleccion - 1][0], listaEventos[eleccionEvento - 1][0])
                eliminarParticipacionLite(listaDeportistasCopy[eleccion - 1][0], listaEventos[eleccionEvento - 1][0])

                eliminarDeportistaDB(listaDeportistasCopy[eleccion - 1][0])
                eliminarDeportistaLite(listaDeportistasCopy[eleccion - 1][0])

                print("Se ha eliminado la participacion y el deportista ya que no poesia mas participaciones")
            else:
                eliminarParticipacionDB(listaDeportistasCopy[eleccion - 1][0], listaEventos[eleccionEvento - 1][0])
                eliminarParticipacionLite(listaDeportistasCopy[eleccion - 1][0], listaEventos[eleccionEvento - 1][0])

                print("Se ha eliminado la participacion")
        else:
            print("Este deportista no tiene participaciones")
    else:
        print("No se encontro ningun deportista que contenga ese nombre")


def anadirParticipacionODeportista():
    listaDeportistas = listarDeportistas()

    nombre = input("Escribe el nombre o parte del nombre del deportista que quieras")

    listaDeportistasCopy = []

    for d in listaDeportistas:
        if nombre.lower() in d[1].lower():
            listaDeportistasCopy.append(d)

    if bool(listaDeportistasCopy):
        contadorDeportista = 0
        for d in listaDeportistasCopy:
            contadorDeportista +=1
            print(str(contadorDeportista) + "- " + d[1])

        # Bucle para que el usuario elija un deportista
        while True:
            try:
                eleccion = int(input("Porfavor elija un deportista de la lista usando el numero"))

                if eleccion <= len(listaDeportistasCopy):
                    print("entro en el if")
                    idDeportista = listaDeportistasCopy[eleccion - 1][0]
                    break

            except:
                print("Debe de introducir un numero del 1 al " + str(contadorDeportista))
    else:
        nombre = crearDeportista()

        idDeportista = DeportistaPorNombreLite(nombre)[0]

    while True:
        eleccion = input("elegir temporada: Summer (S) o Winter (W)").upper()

        if eleccion == "S":
            temporada = "Summer"
            break

        if eleccion == "W":
            temporada = "Winter"
            break

    idOlimpiadaNombre = selecionPorID(listarOlimpiadasXTemporada(temporada), 1, "Nombre Olimpiada")
    idDeporteNombre = selecionPorID(listarDeporteXOlimpiada(idOlimpiadaNombre[0]), 1, "Nombre deporte")
    idEventoNombre = selecionPorID(listarEventosXOlimpiadaXDeporte(idOlimpiadaNombre[0], idDeporteNombre[0]), 1,
                                   "Nombre evento")

    listaEquipos = listarEquiposDB()

    contadorEquipo = 0
    for e in listaEquipos:
        contadorEquipo += 1
        print(contadorEquipo, "- ", e[1])

    while True:
        try:
            elecionEquipo = int(input("Seleciona uno de los equipos con el numero"))

            if elecionEquipo <= len(listaEquipos):
                idEquipo = listaEquipos[elecionEquipo - 1][0]
                break

        except:
            print("Porfavor indicalo con un numero")

    while True:
        try:
            edad = int(input("Introduce la edad que tenia el deportista en su participacion"))
            break

        except:
            print("Porfavor usa un numero")

    while True:
        try:
            print("Elije por que medalla deseas cambiarlo")
            print("1. Gold")
            print("2. Silver")
            print("3. bronze")
            print("4. N/A")

            eleccionMedalla = int(input("Porfavor elija un evento de la lista usando el numero"))

            if eleccionMedalla == 1:
                medalla = "Gold"
                break

            if eleccionMedalla == 2:
                medalla = "Silver"
                break

            if eleccionMedalla == 3:
                medalla = "bronze"
                break

            if eleccionMedalla == 4:
                medalla = "N/A"
                break

        except:
            print("Elije una medalla mediante los numeros porfavor")

    crearParticipacionLite(str(idDeportista[0]), str(idEventoNombre[0]), str(idEquipo), str(edad), str(medalla))
    crearParticipacionDB(idDeportista[0], idEventoNombre[0], idEquipo, edad, medalla)


def crearDeportista():
    nombre = input("Nombre del deportista")

    while True:
        print("Elije el genero del Deportista")
        print("1. Masculino")
        print("2. Femenino")
        try:
            elecionGenero = int(input())

            if elecionGenero == 1:
                genero = "M"
                break

            if elecionGenero == 2:
                genero = "F"
                break
        except:
            print("Elije uno del os dos generos con el numero correspondiente porfavor")

    while True:
        try:
            peso = input("Introduce el peso del deportista, si no se escribe nada se tomara como 0")

            if peso == "":
                peso = 0
                break
            else:
                int(peso)
                break
        except:
            print("Porfavor usa un numero o deja vacio el campo")

    while True:
        try:
            altura = input("Introduce el altura del deportista, si no se escribe nada se tomara como 0")

            if altura == "":
                altura = 0
                break
            else:
                int(altura)
                break
        except:
            print("Porfavor usa un numero o deja vacio el campo")

    crearDeportistaUsuarioDB(nombre, genero, peso, altura)
    crearDeportistaUsuarioLite(nombre, genero, peso, altura)

    print("Se ha creado el deportista " + nombre)

    return nombre


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
            modificarMedallaDB()

        if opcion == 6:
            anadirParticipacionODeportista()

        if opcion == 7:
            eliminarParticipacionDB()

        if opcion == 0:
            finalizar = False


if __name__ == '__main__':
    anadirParticipacionODeportista()