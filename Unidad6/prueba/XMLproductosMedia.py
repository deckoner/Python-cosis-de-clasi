from pyexistdb import db, patch
# patch.request_patching(patch.XMLRpcLibPatch )
conexion = db.ExistDB("http://admin:password@localhost:8080/exist/")
# conexion.removeCollection("almacen")
# if conexion.hasCollection("almacen"):
#     print("La coleccion ya existe")
# else:
#     conexion.createCollection("almacen")

with open ("zonas.xml", encoding="ISO-8859-1") as f:
    xml = f.read()
    print(xml)
conexion.load(xml, "almacen/zonas.xml")
# query = """for $producto in /productos/produc
#            where avg(//precio)<$producto/precio and ($producto/cod_zona=20 or $producto/cod_zona=10)
#        return <product>
#                    <denominacion>{$producto/denominacion/text()}</denominacion>
#                    <precio>{$producto/precio/text()}</precio>
#                </product>"""

query = """for $producto in doc("almacen/productos")//produc
        let $zona := doc("almacen/zonas.xml")//zona[cod_zona=$producto/cod_zona]
        return <produc>
                    <denominacion>{$producto/denominacion/text()}</denominacion>
                    <nombre>{$zona/nombre/text()}</nombre>
                    <director>{$zona/director/text()}</director>
                </produc>"""
q=conexion.executeQuery(query)
xmlFinal = "<temp>"
for i in range(conexion.getHits(q)):
    xmlFinal+=(str)(conexion.retrieve(q,i))
xmlFinal+="</temp>"
conexion.load(xmlFinal,"almacen/almacenMedia2.xml")