import csv
import pickle
from xml.etree import ElementTree as ET
from xml.dom import minidom

class Batalla():

    def __init__(self, id, nombre, anio, region, localizacion, reyAtacante, reyDefensor, ganaAtacante):
        self.id = id
        self.nombre = nombre
        self.anio = anio
        self.region = region
        self.localizacion = localizacion
        self.reyAtacante = reyAtacante
        self.reyDefensor = reyDefensor
        self.ganaAtacante = ganaAtacante

    def __str__(self):

        if self.ganaAtacante == True:
            resultado = "he win"
        else:
            resultado = "the loose"

        cadena = "The " + str(self.nombre) + " took place in " + str(self.localizacion) + " (" + str(self.region) + ") in the year " + str(self.anio) + " The king(s) " + str(self.reyAtacante) + " fought against " + str(self.reyDefensor) + " and " + resultado
        return cadena


def buscarBatallaRegion():
    encontrado = False

    nombreRegion = input("Porfavor ingresa el nombre de la region")

    with open("battles.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row["region"] == nombreRegion):
                encontrado = True

                if row["attacker_king"] == "":
                    atacante = "no king"
                else:
                    atacante = row["attacker_king"]

                if row["defender_king"] == "":
                    defensor = "no king"
                else:
                    defensor = row["defender_king"]

                if row["attacker_outcome"] == "win":
                    resultado = "victoria para el bando atacante"
                else:
                    resultado = "derrota para el bando atacante"

                print(atacante + " Establecio batalla contra el rey " + defensor + " en la region de " + row["region"] +
                      " en la localidad " + row["location"]  + " en el años " + row["year"] + " Fue una " + resultado)

    if encontrado == False:
        print("No se encontro ninguna batalla en esa region o el nombre de la region escrita es incorrecto")


def crearXMLbatalla():
    listaBatallas = [[]]

    with open('battles.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        listaBatallas = list(csv_reader)

    listaBatallas.pop(0)

    root = ET.Element("juego_tronos")

    for campo in listaBatallas:

        batalla = ET.Element("batalla")
        batalla.set("id", campo[2])

        nombre = ET.Element("name")
        nombre.text = campo[0]

        anio = ET.Element("anio")
        anio.text = campo[1]

        region = ET.Element("region")
        region.text = campo[23]

        if campo[23] == "":
            localizacion = ET.Element("localizacion")
            localizacion.text = "no place"
        else:
            localizacion = ET.Element("localizacion")
            localizacion.text = campo[22]

        #Agregamos los ijos de batalla
        batalla.append(nombre)
        batalla.append(anio)
        batalla.append(region)
        batalla.append(localizacion)

        #Comprobamos si fue una derrota o victoria
        if campo[13] == "win":
            atacanteResultado = "s"
            defensorResultado = "n"
        else:
            atacanteResultado = "n"
            defensorResultado = "s"

        #Comprobamos el tamaño del ejercito
        if not campo[17] == "":
            tamanio = campo[17]
        else:
            tamanio = "0"

        #Creamos ataque que tendra varios hijos
        ataque = ET.Element("ataque")
        ataque.set("tamanio", tamanio)
        ataque.set("gana", atacanteResultado)

        if campo[3] == "":
            rey = ET.Element("rey")
            rey.text = "No king"
        else:
            rey = ET.Element("rey")
            rey.text = campo[3]

        comandante = ET.Element("comandante")
        comandante.text = campo[19]

        familia = ET.Element("familia")
        familia.text = campo[5]

        #añadimos a ataque los hijos fijos que va a tener
        ataque.append(rey)
        ataque.append(comandante)
        ataque.append(familia)

        #COmprobamos si existen otras familias y las añadimos
        if not campo[6] == "":
            familia = ET.Element("familia")
            familia.text = campo[6]
            ataque.append(familia)

        if not campo[7] == "":
            familia = ET.Element("familia")
            familia.text = campo[7]
            ataque.append(familia)

        if not campo[8] == "":
            familia = ET.Element("familia")
            familia.text = campo[8]
            ataque.append(familia)

        #Añadimos el ataque a la batalla
        batalla.append(ataque)

        #Comprobamos el tamaño del ejercito
        if not campo[18] == "":
            tamanio = campo[18]
        else:
            tamanio = "0"

        # Creamos ataque que tendra varios hijos
        defensa = ET.Element("defensa")
        defensa.set("tamanio", tamanio)
        defensa.set("gana", defensorResultado)

        if campo[4] == "":
            rey = ET.Element("rey")
            rey.text = "No king"
        else:
            rey = ET.Element("rey")
            rey.text = campo[4]

        comandante = ET.Element("comandante")
        comandante.text = campo[20]

        familia = ET.Element("familia")
        familia.text = campo[9]

        # añadimos a ataque los hijos fijos que va a tener
        defensa.append(rey)
        defensa.append(comandante)
        defensa.append(familia)

        # COmprobamos si existen otras familias y las añadimos
        if not campo[10] == "":
            familia = ET.Element("familia")
            familia.text = campo[10]
            defensa.append(familia)

        if not campo[7] == "":
            familia = ET.Element("familia")
            familia.text = campo[11]
            defensa.append(familia)

        if not campo[8] == "":
            familia = ET.Element("familia")
            familia.text = campo[12]
            defensa.append(familia)

        #Añadimos la defensa a la batalla
        batalla.append(defensa)

        #Añadimos la batalla al elemento root
        root.append(batalla)

    str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
    f = open("battles.xml", "a")
    f.write(str)
    f.close()

    print("Se ha creado el archivo xml con exito")


def crearBinariobatalla():
    with open("battles.bin", "wb") as f:
        raiz = ET.parse("battles.xml").getroot()
        lista = raiz.findall("batalla")
        for e in lista:
            id = e.get("id")
            nombre = e.find("name").text
            anio = e.find("anio").text
            region = e.find("region").text
            localizacion = e.find("localizacion").text

            victoria = e.get("gana")
            if victoria == "win":
                ganaAtacante = True
            else:
                ganaAtacante = False

            #No he conseguido leer dentro de ataque y defensa por eso les pongo el texto de none
            reyAtacante = "None"
            reyDefensor = "None"

            b = Batalla(id, nombre, anio, region, localizacion, reyAtacante, reyDefensor, ganaAtacante)
            pickle.dump(b, f)


def eliminarBatallaBinario():
    id = input("Introduce el ID de la batalla porfavor")

    listaBatallas = []
    borrado = False
    with open("battles.bin", "rb") as f:
        while True:
            try:
                b = pickle.load(f)
                listaBatallas.append(b)
            except EOFError:
                break

    for batalla in listaBatallas:
        if batalla.id == id:
            print(batalla)
            eleccion = int(input("Estas seguro de que quieres borrar la batalla, escribe 1 o para no borrarla escribe cualquier otra cosa"))

            if eleccion == 1:
                listaBatallas.remove(batalla)
                borrado = True

    with open("battles.bin", "wb") as f:
        for batalla in listaBatallas:
            pickle.dump(batalla, f)

    if not borrado:
        print("No se ha encontrado ninguna batalla con ese ID o has decidido no borrarlo")



def menu():

    finalizar= True
    while(finalizar):
        print("""
        1.Buscar batallas por region
        2.Crear XML batallas
        3.Crear fichero bunario objetos
        4.Eliminar batalla fic.Binario objetos
        
        0.Salir
        """)

        eleccion = input("Porfavor introduzca una opcion usando los numeros del menu")

        if eleccion == "1":
            buscarBatallaRegion()

        if eleccion == "2":
            crearXMLbatalla()

        if eleccion == "3":
            crearBinariobatalla()

        if eleccion == "4":
            eliminarBatallaBinario()

        if eleccion == "0":
            finalizar = False


if __name__ == '__main__':
    menu()