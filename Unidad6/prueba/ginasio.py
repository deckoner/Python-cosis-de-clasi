from pyexistdb import db, patch


def _conexion():
     # Creamos la conecxion a la base de datos
    conexion = db.ExistDB("http://admin:admin@localhost:8080/exist/")
    return conexion


def _subirXML():
    # Creamos la conecxion a la base de datos
    conexion = _conexion()

    # Comprobamos si la coleccion ginasio existe, si no existe la creamos
    if conexion.hasCollection("zona"):
        print("La coleccion ya existe")
    else:
        conexion.createCollection("zona")

    #Procedemos a leer los xml y subirlos
    with open("zonas.xml", encoding="ISO-8859-1") as f:
        xml = f.read()
        print(xml)
    conexion.load(xml, "zona/zonas.xml")


def _xmlIntermedio():
    conexion = _conexion()

    query = """for $dato in doc("ginasio/uso_gimnasio.xml")//fila_uso
                let $actividad := doc("ginasio/actividades_gim.xml")//fila_actividades[@cod = $dato/CODACTIV]
                let $socio := doc("ginasio/socios_gim.xml")//fila_socios[COD = $dato/CODSOCIO]
                let $horas := $dato/HORAFINAL - $dato/HORAINICIO

                return <dato>
                            <COD>{$socio/COD/text()}</COD>
                            <NOMBRESOCIO>{$socio/NOMBRE/text()}</NOMBRESOCIO>
                            <CODACTIV>{$dato/CODACTIV/text()}</CODACTIV>
                            <NOMBREACTIVIDAD>{$actividad/NOMBRE/text()}</NOMBREACTIVIDAD>
                            <horas>{$horas}</horas>
                            <tipoact>{$actividad/@tipo/data()}</tipoact>
                            {if ($actividad/@tipo = 3) then <cuota_adicional>{4 * $horas}</cuota_adicional>
                            else if ($actividad/@tipo = 2) then <cuota_adicional>{2 * $horas}</cuota_adicional>
                            else <cuota_adicional>0</cuota_adicional>}
                       </dato>
                """
    q = conexion.executeQuery(query)

    xmlFinal = "<temp>"

    for i in range(conexion.getHits(q)):
        xmlFinal += (str)(conexion.retrieve(q, i))
    xmlFinal += "</temp>"
    print(xmlFinal)
    conexion.load(xmlFinal, "ginasio/intermedio.xml")


def insertar():
    conexion = _conexion()
    codzona= 50
    nombre = "pepe"
    directo = "perso"

    query = """update insert <zona><cod_zona>%s</cod_zona><nombre>%s</nombre><director>%s</director> </zona> into doc("zona/zonas.xml")/zonas""" %(codzona, nombre, directo)

    conexion.executeQuery(query)

def existeZona():
    conexion = _conexion()
    zona = 10

    query = """let $zone := doc("zona/zonas.xml")/zonas/zona[cod_zona=%s]
    return $zone""" %(zona)

    result = conexion.executeQuery(query)
    if conexion.getHits(result):
        print("La zona %s existe." %zona)
    else:
        print("La zona %s no existe." %zona)


if __name__ == '__main__':
    existeZona()
