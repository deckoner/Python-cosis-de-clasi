import csv
from csv import Dialect
from xml.etree import ElementTree as ET
from xml.dom import minidom

def crearXMLOlimpiadas():

    listaOlimpiadas = [[]]

    with open('olimpiadas.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        listaOlimpiadas = list(csv_reader)

    listaOlimpiadas.pop(0)
    listaOlimpiadas = sorted(listaOlimpiadas, key=lambda x: (x[2], x[1]), reverse=True)

    root = ET.Element("olimpiadas")

    for campo in listaOlimpiadas:
        olimppiada = ET.Element("olimpiada")
        olimppiada.set("year", campo[1])

        juegos = ET.Element("juegos")
        juegos.text = campo[0]

        temporada = ET.Element("temporada")
        temporada.text = campo[2]

        ciudad = ET.Element("ciudad")
        ciudad.text = campo[3]

        olimppiada.append(juegos)  #añadimos hijos
        olimppiada.append(temporada)
        olimppiada.append(ciudad)

        root.append(olimppiada)  #Lo añadimos a la raiz

    str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
    f = open("olimpiadas.xml", "a")
    f.write(str)
    f.close()

    print("Se ha creado el archivo xml con exito")

def crearXMLdeportistas():
    listaDeportistas = [[]]

    with open('olimpiadas.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        listaDeportistas = list(csv_reader)

    listaDeportistas.pop(0)

    root = ET.Element("olimpiadas")

    for campo in listaDeportistas:
        olimppiada = ET.Element("olimpiada")
        olimppiada.set("year", campo[1])

        juegos = ET.Element("juegos")
        juegos.text = campo[0]

        temporada = ET.Element("temporada")
        temporada.text = campo[2]

        ciudad = ET.Element("ciudad")
        ciudad.text = campo[3]

        olimppiada.append(juegos)  #añadimos hijos
        olimppiada.append(temporada)
        olimppiada.append(ciudad)

        root.append(olimppiada)  #Lo añadimos a la raiz

    str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
    f = open("olimpiadas.xml", "a")
    f.write(str)
    f.close()

if __name__ == '__main__':
    while finalizar == True:
        print("""
        1.Crear fichero XML de olimpiadas
        2.Crear un fichero XML de deportistas
        3.Listado de olimpiadas

        0.Salir
        """)

        opcion = int(input("Porfavor elige una opcion escribiendo un numero"))

        if opcion == 1:
            crearXMLOlimpiadas()

        if opcion == 2:
            pass

        if opcion == 3:
            pass

        if opcion == 0:
            finalizar = False
    crearXMLOlimpiadas()