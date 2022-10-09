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

    def buscarAtleta(self, nombreAtleta):

        fase = True
        encontrado = False

        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            columnas = ["Name", "Sex", "Age", "Height", "Weight", "NOC", "Games", "Year", "Season", "City", "Sport", "Event"]

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

    def buscardeportistaOlimpiada(self, deporte, year, temporada):

        fase = True
        encontrado = False

        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            columnas = ["Sport", "Year", "Season", "Games", "City", "Name", "Event", "Medal"]

            for row in reader:





                if (fase == True):
                    if (row["Name"] == nombreAtleta):
                        encontrado = True
                        fase = False

                        print(nombreAtleta + " Años: " + row["Age"] + " Genero: " + row["Sex"] + " Altura: " + row[
                            "Height"] +
                              " Peso: " + row["Weight"] + " Equipo: " + row["Team"] + " Nacionalidad: " + row["NOC"])
                        print("Participaciones:")
                        print("\tAño: " + row["Year"] + ", " + row["Games"] + " de " + row["Season"] + " en " +
                              row["City"] + " participo en " + row["Sport"] + " en el evento " + row["Event"])
                else:
                    if (row["Name"] == nombreAtleta):
                        print("\tAño: " + row["Year"] + ", " + row["Games"] + " de " + row["Season"] + " en " +
                              row["City"] + " participo en " + row["Sport"] + " en el evento" + row["Event"])

        if (encontrado == False):
            print("No se se encontro atleta")


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
        c.buscarAtleta(nombre)

    if opcion == 3:
        pass

    if opcion == 4:
        pass

    if opcion == 0:
        finalizar = False