from pyexistdb import db, patch

#patch.request_patching(patch.XMLRpcLibPatch)
db = db.ExistDB("http://admin:password@localhost:8080/exist/")

db.removeCollection("empresa")
# Creamos la colección/base de datos en caso de que no esté creada (Una colección es donde se guardan los archivs xml)
if db.hasCollection("empresa"):
    print("La colección existe")
else:
    db.createCollection("empresa")

# ----------------------------------------------------------------------------------------------------------------

# Subimos el archivo a la coleccion leyendo el fichero y con el metodo load
# (Si no ponemos el encoding que viene al inicio del xml da error)

with open("T6_empleados.xml", encoding="ISO-8859-1") as f:
    xml = f.read()
    print(xml)

db.load(xml, "empresa/empleados.xml")

# El executeQuery devuelve el id de la consulta FLWOR For Let Where Order by y Return (obligatorios f y r)
# Emple es como queremos llamar a los nuevos nodos solo con al información del apellido y que tengan mas de 2000 de salario
query = """
for $empleado in //EMP_ROW
where $empleado/SALARIO >= 2000
return 
    <emple>
        <apellido>{$empleado/APELLIDO/text()}</apellido>
        <salario>{$empleado/SALARIO/text()}</salario>
    </emple>
"""

# Guardamos el id de la query cuando se ejecute
q = db.executeQuery(query)

# Creamos el nuevo xml
xmlFinal = "<NuevoXML>"
print(q, db.getHits(q))
# El gethits nos dice cuantos nodos han sido afectados
for i in range(db.getHits(q)):
    # a xml final le añade
    xmlFinal += str(db.retrieve(q, i))
xmlFinal += "</NuevoXML>"

db.load(xmlFinal, "empresa/empleadoCorto.xml")

