from pyexistdb import db, patch

conexion = db.ExistDB("http://admin:admin@localhost:8080/exist/")

if conexion.hasCollection("almacen"):
    print("La coleccion ya existe")
else:
    conexion.createCollection("almacen")

with open ("zonas.xml", encoding="ISO-8859-1") as f:
    xml = f.read()
conexion.load(xml, "empresa/zonas.xml")
query = """for $zona in doc("empresa/zonas.xml")//zona
            let $sumaZona := sum(doc("almacen/productos.xml")//produc[cod_zona=$zona/cod_zona]/stock_actual) 
            
            return <zona>
                        {if ($zona/cod_zona = 10) then <cod_zona>Zona A</cod_zona>
                        else if ($zona/cod_zona = 20) then <cod_zona>Zona B</cod_zona>
                        else if ($zona/cod_zona = 30) then <cod_zona>Zona C</cod_zona>
                        else <cod_zona>Zona C</cod_zona>}
                        <stockTotal>{$sumaZona}</stockTotal>
                   </zona>
            """
q = conexion.executeQuery(query)

xmlFinal = "<temp>"

for i in range(conexion.getHits(q)):
    xmlFinal += (str)(conexion.retrieve(q,i))
xmlFinal += "</temp>"
print(xmlFinal)
conexion.load(xmlFinal, "empresa/ProductosPorZonas.xml")