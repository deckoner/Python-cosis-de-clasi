import csv


class CSVobjeto:

    def crearCsvOlimpiadas(self):
        olimpiadas = []

        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)

            with open("olimpiadas.csv", 'w', newline="") as csvolimpiadas:
                columnas = ["Games","Year","Season","City"]
                writer = csv.DictWriter(csvolimpiadas,columnas)
                writer.writeheader()

                for row in reader:
                    if not row["Games"] in olimpiadas:
                        olimpiadas.append(row["Games"])
                        writer.writerow({columnas[0]:row["Games"],columnas[1]:row["Year"],columnas[2]:row["Season"],columnas[3]:row["City"]})
        print("Se ha creado el fichero con exito")

    def buscarAtleta(self):

        fase = True
        encontrado = False

        nombreAtleta = input("Porfavor ingresa el nombre y apellidos del atleta")

        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if (fase == True):
                    if (row["Name"] == nombreAtleta):

                        encontrado = True
                        fase = False

                        print(nombreAtleta + " Años: " + row["Age"] + " Genero: " + row["Sex"] + " Altura: " + row["Height"] +
                              " Peso: " + row["Weight"] + " Equipo: " + row["Team"] + " Nacionalidad: " + row["NOC"])
                        print("Participaciones:")
                        print("\tAño: " + row["Year"] + ", " + row["Games"] + " de " + row["Season"] + " en " +
                              row["City"] + " participo en " + row["Sport"]+ " en el evento " + row["Event"])
                else:
                    if (row["Name"] == nombreAtleta):
                        print("\tAño: " + row["Year"] + ", " + row["Games"] + " de " + row["Season"] + " en " +
                              row["City"] + " participo en " + row["Sport"] + " en el evento" + row["Event"])

        if (encontrado == False):
            print("No se se encontro atleta")

    def buscardeportistaOlimpiada(self):
        encontrado = False

        deporte = input("Porfavor introduszca un deporte")
        year = input("Porfavor intoduzca un año")
        temporada = input("Porfavor introduzca una temporada")

        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if (row["Sport"] == deporte and row["Year"] == year and row["Season"] == temporada):

                    if encontrado == False:
                        encontrado = True
                        print(row["Games"] + "celebrado en " + row["City"] + " deporte: " + row["Sport"])
                        print("Lista de participantes:")

                    print("\tNombre: " + row["Name"] + " Evento: " + row["Event"] + " Medalla: " + row["Medal"])

            if (encontrado == False):
                print("No se se encontro ninguna edicion olimpica")

    def anadirDeportista(self):
        id = input("ID del deportista")
        name = input("Nombre del deportista")
        sex = input("Genero del deportista")
        age = input("Años del deportista")
        height = input("Altura del deportista")
        weight = input("Peso del deportista")
        team = input("Equipo del deportista")
        noc = input("Nacionalidad del deportista")
        games = input("Los juegos en el que participa")
        year = input("Año en el que participa")
        seasson = input("La temporada en la que participo")
        city = input("Ciudad de los juegos")
        sport = input("Deporte donde participo")
        event = input("Nombre del evento donde participo")
        medal = input("Medalla ganada en el evento")

        datos = [(id, name, sex, age, height, weight, team, noc, games, year, seasson, city, sport, event, medal)]
        csvsalida = open('athlete_events.csv', 'a', newline='')
        salida = csv.writer(csvsalida)
        salida.writerows(datos)
        csvsalida.close()

c = CSVobjeto()

finalizar = True

while finalizar == True:
    print("""
    1.Generar fichero csv de olimpiadas
    2.Buscar deportista
    3.Buscar deportistas por deporte y olimpiada
    4.Añadir deportista

    0.Salir
    """)

    opcion = int(input("Porfavor elige una opcion escribiendo un numero"))

    if opcion == 1:
        c.crearCsvOlimpiadas()

    if opcion == 2:
        nombre = input("Porfavor ingresa el nombre y apellidos del atleta")
        c.buscarAtleta()

    if opcion == 3:
        c.buscardeportistaOlimpiada()

    if opcion == 4:
        c.anadirDeportista()

    if opcion == 0:
        finalizar = False