from xml.etree import ElementTree as ET
from xml.dom import minidom

lista = [["1", "Mikel", "infor"], ["2", "Fernando", "administracion"], ["3", "Juan", "comercio"]]

root = ET.Element("alumnos")

for i in lista:
    alumno = ET.Element("alumno")
    alumno.set("id",i[0])

    nombre = ET.Element("nombre")
    nombre.text = i[1]

    departamento = ET.Element("departamento")
    departamento.text = i[2]

    alumno.append(nombre) #añadimos hijos
    alumno.append(departamento)

    root.append(alumno) #Lo añadimos a la raiz

print(ET.tostring(root))
str = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "\t")
f = open("alumnos.xml", "a")
f.write(str)
f.close()

f = open("alumnos.xml")
raiz = ET.parse("alumnos.xml").getroot()
lista = raiz.findall("alumno")

for i in lista:
    id = i.get("id")
    nombre = i.find("nombre").text
    departamento = i.find("departamento").text
    print(id+  "----" + nombre + "----" + departamento)