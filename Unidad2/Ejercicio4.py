from xml.etree import ElementTree as ET
import pickle


class olimpiada():

    def __init__(self, year, juegos, temporada, ciudad):
        self.year = year
        self.juegos = juegos
        self.temporada = temporada
        self.ciudad = ciudad

    def verOlimpiada(self):
        print("Año: " + self.year + " Juegos: " + self.juegos + " Temporada: " + self.temporada + "Ciudad: "
              + self.ciudad)


def leerOlimpiadasBinarias():
    with open("olimpiadas.pickle", "rb") as f:
        while True:
            try:
                alumno = pickle.load(f)
                alumno.verOlimpiada()
            except EOFError:
                break

def crearObjetosOlimpiadas():
    with open("olimpiadas.pickle", "wb") as f:
        raiz = ET.parse("olimpiadas.xml").getroot()
        lista = raiz.findall("olimpiada")
        for al in lista:
            year = al.get("year")
            juegos = al.find("juegos").text
            temporada = al.find("temporada").text
            ciudad = al.find("ciudad").text

            o = olimpiada(year, juegos, temporada, ciudad)

            pickle.dump(o, f)

def anadirOlimpiada():

    year = input("Año de la olimpiada")
    juegos = input("Nombre de los juegos")
    temporada = input("temporada de la olimpiada")
    ciudad = input("Ciudad donde se celebro")

    o = olimpiada(year, juegos, temporada, ciudad)
    listaOlimpiadas = []
    listaOlimpiadas.append(o)

    with open("olimpiadas.pickle", "rb") as f:
        while True:
            try:
                o = pickle.load(f)
                listaOlimpiadas.append(o)

            except EOFError:
                break

    with open("olimpiadas.pickle", "wb") as f:
        for olimpiadaLista in listaOlimpiadas:
            pickle.dump(olimpiadaLista, f)

    leerOlimpiadasBinarias()

def buscarOlimpiadaSede():
    leerOlimpiadasBinarias()
    ciudad = input("Porfavor introduzca el nombre de la ciudad, la primera en mayusculas")
    encontrado = False
    with open("olimpiadas.pickle", "rb") as f:
        while True:
            try:
                o = pickle.load(f)
                if o.ciudad == ciudad:
                    o.verOlimpiada()
                    encontrado = True
            except EOFError:
                break
    if not encontrado:
        print("No ahi ninguna olimpiada registrada en esa sede")

def eliminarOlimpiadaBinario():
    yearUser = input("Intorduce el año de la olimpiada a borrar")
    temporadaUser = input("introduce la temporada del año a borrar")

    listaOlimpiadas = []

    borrado = False

    with open("olimpiadas.pickle", "rb") as f:
        while True:
            try:
                o = pickle.load(f)
                listaOlimpiadas.append(o)

            except EOFError:
                break

    for o in listaOlimpiadas:
        if o.year == yearUser and o.temporada == temporadaUser:
            listaOlimpiadas.pop(o)
            borrado = True

    with open("olimpiadas.pickle", "wb") as f:
        for olimpiadaLista in listaOlimpiadas:
            pickle.dump(olimpiadaLista, f)

    if not borrado:
        print("No se ha encontrado ninguna edicion olimpica con esa informacion")

def eliminarOlimpiada():
    pass

if __name__ == '__main__':

    finalizar = True

    while finalizar == True:
        print("""
        1.Crear fichero serializado de olimpiadas
        2.añadir edicion olimpica
        3.Buscar olimpiadas por sede
        4.Eliminar edicion olimpica

        0.Salir
        """)

        opcion = int(input("Porfavor elige una opcion escribiendo un numero"))

        if opcion == 1:
            crearObjetosOlimpiadas()

        if opcion == 2:
            anadirOlimpiada()

        if opcion == 3:
            buscarOlimpiadaSede()

        if opcion == 4:
            eliminarOlimpiadaBinario()
        if opcion == 0:
            finalizar = False