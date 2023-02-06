from pyexistdb import db, patch


def _conexion():
     # Creamos la conecxion a la base de datos
    conexion = db.ExistDB("http://admin:admin@localhost:8080/exist/")
    return conexion


def _subirXML():
    # Creamos la conecxion a la base de datos
    conexion = _conexion()

    # Comprobamos si la coleccion ginasio existe, si no existe la creamos
    if conexion.hasCollection("ginasio"):
        print("La coleccion ya existe")
    else:
        conexion.createCollection("ginasio")

    #Procedemos a leer los xml y subirlos
    with open("socios_gim.xml", encoding="ISO-8859-1") as f:
        xml = f.read()
        print(xml)
    conexion.load(xml, "ginasio/socios_gim.xml")

    with open("uso_gimnasio.xml", encoding="ISO-8859-1") as f:
        xml = f.read()
        print(xml)
    conexion.load(xml, "ginasio/uso_gimnasio.xml")

    with open("actividades_gim.xml", encoding="ISO-8859-1") as f:
        xml = f.read()
        print(xml)
    conexion.load(xml, "ginasio/actividades_gim.xml")


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


def _xmlFinal():
    conexion = _conexion()

    query = """for $socio in doc("ginasio/socios_gim.xml")//fila_socios
                let $cuotaAdicional := sum(doc("ginasio/intermedio.xml")//dato[COD = $socio/COD]/cuota_adicional)

                return <dato>
                            <COD>{$socio/COD/text()}</COD>
                            <NOMBRESOCIO>{$socio/NOMBRE/text()}</NOMBRESOCIO>
                            <CUOTA_FIJA>{$socio/CUOTA_FIJA/text()}</CUOTA_FIJA>
                            <suma_cuota_adic>{$cuotaAdicional}</suma_cuota_adic>
                            <cuota_total>{$cuotaAdicional + $socio/CUOTA_FIJA}</cuota_total>
                       </dato>
                """
    q = conexion.executeQuery(query)

    xmlFinal = "<temp>"

    for i in range(conexion.getHits(q)):
        xmlFinal += (str)(conexion.retrieve(q, i))
    xmlFinal += "</temp>"
    print(xmlFinal)
    conexion.load(xmlFinal, "ginasio/cuotasTotales.xml")

if __name__ == '__main__':
    _xmlIntermedio()
    _xmlFinal()
