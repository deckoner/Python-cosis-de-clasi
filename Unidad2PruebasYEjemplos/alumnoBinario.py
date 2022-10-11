from xml.etree import ElementTree as ET
import pickle

class Alumno():
    def __init__(self, id, nombre, departamento):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento

    def verAlumno(self):
        print("id: "+self.id+" nombre: "+self.nombre+" departamento: "+self.departamento)


with open("alumnos.pickle", "wb") as f:
    raiz = ET.parse("alumnos.xml").getroot()
    lista = raiz.findall("alumno")
    for al in lista:
        id = al.get("id")
        nombre = al.find("nombre").text
        departamento = al.find("departamento").text

        alumno = Alumno(id, nombre, departamento)

        pickle.dump(alumno, f)

with open("alumnos.pickle", "rb") as f:
    while True:
        try:
            alumno = pickle.load(f)
            alumno.verAlumno()

        except EOFError:
            break

alumno = Alumno("4", "Andoni", "Administracion")

with open("alumnos.pickle", "ab") as f:
    pickle.dump(alumno, f)

with open("alumnos.pickle", "rb") as f:
    while True:
        try:
            alumno = pickle.load(f)
            alumno.verAlumno()

        except EOFError:
            break

nombre = input("Introduce nombre a buscar")

with open("alumnos.pickle", "rb") as f:
    while True:
        try:
            alumno = pickle.load(f)

            if alumno.nombre == nombre:
                alumno.verAlumno()

        except EOFError:
            break
