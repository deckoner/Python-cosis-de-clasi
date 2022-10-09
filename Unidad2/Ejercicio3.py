import csv
import xml.sax
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

    with open('athlete_eventsChiquito.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        listaDeportistas = list(csv_reader)

    listaDeportistas.pop(0)

    root = ET.Element("deportistas")

    idActual = listaDeportistas[0][0]
    deporteActual = listaDeportistas[0][12]

    #Metemos parte de la primera lectura a mano para no controlarlo en el bucle
    deportista = ET.Element("deportista")
    deportista.set("id", listaDeportistas[0][0])

    nombre = ET.Element("nombre")
    nombre.text = listaDeportistas[0][1]

    sexo = ET.Element("sexo")
    sexo.text = listaDeportistas[0][2]

    altura = ET.Element("altura")
    altura.text = listaDeportistas[0][4]

    peso = ET.Element("peso")
    peso.text = listaDeportistas[0][5]

    deportista.append(nombre)
    deportista.append(sexo)
    deportista.append(altura)
    deportista.append(peso)

    participaciones = ET.Element("participaciones")

    deporte = ET.Element("deporte")
    deporte.set("nombre", listaDeportistas[0][12])

    for campo in listaDeportistas:
        if not idActual == campo[0]:
            participaciones.append(deporte)
            deportista.append(participaciones)
            root.append(deportista)

            idActual = campo[0]

            deportista = ET.Element("deportista")
            deportista.set("id", campo[0])

            nombre = ET.Element("nombre")
            nombre.text = campo[1]

            sexo = ET.Element("sexo")
            sexo.text = campo[2]

            altura = ET.Element("altura")
            altura.text = campo[4]

            peso = ET.Element("peso")
            peso.text = campo[5]

            deportista.append(nombre)
            deportista.append(sexo)
            deportista.append(altura)
            deportista.append(peso)

            participaciones = ET.Element("participaciones")

        if not deporteActual == campo[12]:
            participaciones.append(deporte)

            deporteActual = campo[12]

            deporte = ET.Element("deporte")
            deporte.set("nombre", campo[12])

        participacion = ET.Element("participacion")
        participacion.set("edad", campo[3])

        equipo = ET.Element("equipo", abbr=campo[7])
        equipo.text = campo[6]

        juegos = ET.Element("juegos")
        juegos.text = (campo[8] + "" + campo[11])

        evento = ET.Element("evento")
        evento.text = campo[13]

        medalla = ET.Element("medalla")
        medalla.text = campo[14]

        participacion.append(equipo)
        participacion.append(juegos)
        participacion.append(evento)
        participacion.append(medalla)

        deporte.append(participacion)

    str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
    f = open("Deportistas.xml", "a")
    f.write(str)
    f.close()

def listarOlimpiadas():
    pass



if __name__ == '__main__':

    finalizar = True

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
            crearXMLdeportistas()

        if opcion == 3:
            listarOlimpiadas()

        if opcion == 0:
            finalizar = False