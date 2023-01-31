from pyexistdb import db, patch
# patch.request_patching(patch.XMLRpcLibPatch )
conexion = db.ExistDB("http://admin:password@localhost:8080/exist/")
conexion.removeCollection("empresa")
if conexion.hasCollection("empresa"):
    print("La coleccion ya existe")
else:
    conexion.createCollection("empresa")

with open ("empleados.xml", encoding="ISO-8859-1") as f:
    xml = f.read()
    print(xml)
conexion.load(xml, "empresa/empleados")
query = """for $empleado in /EMPLEADOS/EMP_ROW  
            where $empleado/SALARIO > 2000
            return <emple>
                        <apellidos>{$empleado/APELLIDO/text()}</apellidos>
                        <salario>{$empleado/SALARIO/text()}</salario>
                   </emple>
            """
q=conexion.executeQuery(query)
xmlFinal = "<temp>"
for i in range(conexion.getHits(q)):
    xmlFinal+=(str)(conexion.retrieve(q,i))
xmlFinal+="</temp>"
conexion.load(xmlFinal,"empresa/empleadoCorto.xml")

