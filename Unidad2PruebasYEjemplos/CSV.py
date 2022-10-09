import csv

class CSV:
    def mostrarAtletas(self):

        cont = 0
        Atletas = []

        with open("../Unidad2/athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if not row["Games"] in Atletas:
                    Atletas.append(row["Games"])
                    print(row["Games"])
                    cont += 1
            print(cont)

    def crearCSVOlimpiadas(self):
        olimpiadas = []
        columnas = []

        with open("../Unidad2/athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)

            with open("../Unidad2/olimpiadas.csv", "w") as olimpiadasCSV:
                writer = csv.DictWriter(olimpiadasCSV, columnas)
                writer.writeheader()
                for row in reader:
                    if not row["Games"] in olimpiadas:
                        writer.writerow()

            for row in reader:
                if not row["Games"] in olimpiadas:
                    olimpiadas.append(row["Games"])
                    print(row["Games"])



if __name__ == '__main__':
    c = CSV()
    c.mostrarAtletas()