from Unidad3.OlimpiadasBD import *
import csv


def crearBaseDatos():
    # Generamos los diccionarios
    equipos = {}
    deportes = []

    with open("athlete_eventsChiquito.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if not row["Team"] in equipos:
                equipos[row["Team"]] = row["NOC"]

            if not row["Sport"] in deportes:
                deportes.append(row["Sport"])

    # Añadimos los equipos a la base de datos
    # for e in equipos:
    #     rellenarEquipo(e, equipos[e])

    for d in deportes:
        rellenarDeporte(d)


if __name__ == '__main__':
    crearBaseDatos()