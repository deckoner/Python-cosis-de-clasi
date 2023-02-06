from pyexistdb import db, patch
conexion = db.ExistDB("http://admin:admin@localhost:8080/exist/")
if conexion.hasCollection("almacen"):
    print("La coleccion ya existe")
else:
    conexion.createCollection("almacen")

with open ("productos.xml", encoding="ISO-8859-1") as f:
    xml = f.read()
    print(xml)
conexion.load(xml, "almacen/productos.xml")
query = """for $producto in /productos/produc  
            where  $producto/stock_minimo < $producto/stock_actual
            return <produc>
                        <denominacion>{$producto/cod_prod/text()}</denominacion>
                        <denominacion>{$producto/denominacion/text()}</denominacion>
                   </produc>
            """
q=conexion.executeQuery(query)
xmlFinal = "<temp>"
for i in range(conexion.getHits(q)):
    xmlFinal+=(str)(conexion.retrieve(q,i))
xmlFinal+="</temp>"
conexion.load(xmlFinal,"almacen/almacen.xml")