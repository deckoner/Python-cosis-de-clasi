from xml.dom import minidom

class olimpiadas():

    def __init__(self):
        self.year = ""
        self.juegos = ""
        self.temporada = ""
        self.ciudad = ""


def crearObjetosOlimpiadas():
    doc = minidom.parse("olimpiadas.xml")
    olimpiadas = doc.getElementsByTagName("olimpiada")
    for olimpiada in olimpiadas:
        sid = olimpiada.getAttribute("year")
        juegos = olimpiada.getElementsByTagName("juegos")[0]
        temporada = olimpiada.getElementsByTagName("temporada")[0]
        ciudad = olimpiada.getElementsByTagName("ciudad")[0]
        o = olimpiadas(sid, juegos.firstChild.data, temporada.firstChild.data, ciudad.firstChild.data)
        print("juegos:%s " % sid)
        print("username:%s" % juegos.firstChild.data)
        print("temporada:%s" % temporada.firstChild.data)
        print("ciudad:%s" % ciudad.firstChild.data)


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
            pass

        if opcion == 3:
            pass

        if opcion == 4:
            pass
        if opcion == 0:
            finalizar = False