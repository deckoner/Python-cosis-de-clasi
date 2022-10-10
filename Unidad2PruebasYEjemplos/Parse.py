import xml.sax as sax

class AlumnosHandler(sax.handler.ContentHandler):

    def __init__(self):
        self.CurrentData = ""

    def startElement(self, tag, atri):
        self.CurrentData = tag
        if tag == "alumno":
            print("alumno con id ", atri["id"])

    def endElement(self, tag):
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "nombre":
            print("Nombre: "+ content)
        if self.CurrentData == "departamento":
            print("Departamento: "+ content)

h = AlumnosHandler()
sax.parse("alumnos.xml", h)