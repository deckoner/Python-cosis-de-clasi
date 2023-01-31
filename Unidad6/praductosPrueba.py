from pyexistdb import db, patch

#patch.request_patching(patch.XMLRpcLibPatch)
db = db.ExistDB("http://admin:admin@localhost:8080/exist/")


def crearDB():
    # Creamos la colección/base de datos en caso de que no esté creada (Una colección es donde se guardan los archivs xml)
    if db.hasCollection("tienda"):
        print("La colección existe")
    else:
        db.createCollection("tienda")


def rellenarDB():
    # Subimos el archivo a la coleccion leyendo el fichero y con el metodo load
    # (Si no ponemos el encoding que viene al inicio del xml da error)
    with open("productos.xml", encoding="ISO-8859-1") as f:
        xml = f.read()
        print(xml)

    db.load(xml, "tienda/todosProductos.xml")

def crearEmpleadosSuelo2000mas():
    # El executeQuery devuelve el id de la consulta FLWOR For Let Where Order by y Return (obligatorios f y r)
    # Emple es como queremos llamar a los nuevos nodos solo con al información del apellido y que tengan mas de 2000 de salario
    query = """
    for $produc in /tienda/todosProductos/productos/produc
    where $produc/stock_actual <= $produc/stock_minimo
    return
        <produc>
            <denominacion>{$produc/denominacion/text()}</denominacion>
        </produc>
    """

    # Guardamos el, id de la query cuando se ejecute
    q = db.executeQuery(query)

    # Creamos el nuevo xml
    xmlFinal = "<NuevoXML>"
    print(q, db.getHits(q))
    # El gethits nos dice cuantos nodos han sido afectados
    for i in range(db.getHits(q)):
        # a xml final le añade
        xmlFinal += str(db.retrieve(q, i))
    xmlFinal += "</NuevoXML>"

    db.load(xmlFinal, "tienda/productosConMasMinimo.xml")


if __name__ == '__main__':
    crearEmpleadosSuelo2000mas()