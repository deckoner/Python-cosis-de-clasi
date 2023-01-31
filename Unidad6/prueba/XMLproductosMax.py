from pyexistdb import db, patch
# patch.request_patching(patch.XMLRpcLibPatch )
conexion = db.ExistDB("http://admin:password@localhost:8080/exist/")
# conexion.removeCollection("almacen")
if conexion.hasCollection("almacen"):
    print("La coleccion ya existe")
else:
    conexion.createCollection("almacen")

with open ("productos.xml", encoding="ISO-8859-1") as f:
    xml = f.read()
    print(xml)
conexion.load(xml, "almacen/productos")
query = """for $producto in /productos/produc  
            where  $producto/precio = max(//$producto/precio) 
            return <produc>
                        <cod_prod>{$producto/cod_prod/text()}</cod_prod>
                        <denominacion>{$producto/denominacion/text()}</denominacion>
                        <precio>{$producto/precio/text()}</precio>
                        <stock_actual>{$producto/stock_actual/text()}</stock_actual>
                        <stock_minimo>{$producto/stock_minimo/text()}</stock_minimo>
                        <cod_zona>{$producto/cod_zona/text()}</cod_zona>
                   </produc>
            """
q=conexion.executeQuery(query)
xmlFinal = "<temp>"
for i in range(conexion.getHits(q)):
    xmlFinal+=(str)(conexion.retrieve(q,i))
xmlFinal+="</temp>"
conexion.load(xmlFinal,"almacen/almacenMax.xml")