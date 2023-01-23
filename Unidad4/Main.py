from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Unidad4.Model.Mapeo import *


# Hacemos una funcion para que nos devuelva una sesion sqlLite
def sqlLite():
    engine = create_engine("sqlite:///enbebido.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ejecutamos esta sentencia para que tenga las Foreign Keys activas
    session.execute('pragma foreign_Keys=on')

    # Devolvemos la funcion ya echa
    return session


# Hacemos una funcion para que nos devuelva una sesion sql
def sql():
    engine = create_engine("mysql+pymysql://admin:password@localhost/olimpiadaspy")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Devolvemos la funcion ya echa
    return session


def listarDeportistasParticipacion():
    # Preguntamos al usuario que base de datos quiere usar
    while True:
        print("1. SQL")
        print("1. SQLLITE")

        elecion = input("Elige una de las dos opciones con los numeros 1 y 2")

        if elecion == "1":
            session = sql()
            break

        if elecion == "2":
            session = sqlLite()
            break

    # Ahora le preguntamos que temporada quiere
    while True:
        print("1. Winter")
        print("2. Summer")

        elecion = input("Porfavor elige una opcion escribiendo 1 o 2")

        if elecion == "1":
            temporada = "Winter"
            break

        if elecion == "2":
            temporada = "Summer"
            break

    # Hacemos la consulta y mostramos la lista de olimpiadas en la fecha señalada
    resultado = session.query(Olimpiada).filter(Olimpiada.temporada == temporada).all()

    # Creamos un diccionario vacio para guardar los IDs de las olimpiadas junto con su numero en la lista
    olimpiadaDiccionario = {}
    totalOlimpiada = 0

    for o in resultado:
        totalOlimpiada += 1
        olimpiadaDiccionario[totalOlimpiada] = o.id_olimpiada
        print(str(totalOlimpiada) + "." + o.nombre)

    while True:
        elecion = input("Seleciona escribiendo el numero de la olimpiada que quieres")

        if int(elecion) <= totalOlimpiada:
            idOlimpiada = olimpiadaDiccionario[int(elecion)]
            break

    # Consultamos los deportes de la edicion Olimpica
    olimpiada = session.query(Olimpiada).filter(Olimpiada.id_olimpiada == idOlimpiada).one()

    # Creamos un diccionario vacio para guardar los IDs de las olimpiadas junto con su numero en la lista
    deporteDiccionario = {}
    totalDeporte = 0

    for e in olimpiada.eventos:
        totalDeporte += 1
        deporteDiccionario[totalDeporte] = e.id_deporte
        print(str(totalDeporte) + "." +e.deporte.nombre)

    while True:
        elecion = input("Seleciona escribiendo el numero del deporte que quieres")

        if int(elecion) <= totalDeporte:
            idDeporte = deporteDiccionario[int(elecion)]
            break

    # Consultamos los Eventos de la edicion Olimpica con los deportes
    evento = session.query(Evento).filter(Evento.id_olimpiada == idOlimpiada, Evento.id_deporte == idDeporte)

    # Creamos un diccionario vacio para guardar los IDs de los eventos junto con su numero en la lista
    eventoDiccionario = {}
    totalEvento = 0

    for e in evento:
        totalEvento += 1
        eventoDiccionario[totalEvento] = e.id_evento
        print(str(totalEvento) + "." + e.nombre)

    while True:
        elecion = input("Seleciona escribiendo el numero del evento que quieres")

        if int(elecion) <= totalEvento:
            idEvento = eventoDiccionario[int(elecion)]
            break

    evento = session.query(Evento).filter(Evento.id_evento == idEvento).one()

    print("Temporada: " + str(olimpiada.temporada) +
          "\nEdicion Olimpica: " + olimpiada.nombre +
          "\nDeporte: " + evento.deporte.nombre +
          "\nEvento: " + evento.nombre)

    for p in evento.participaciones:
        print("-----------------------------------------")
        print("\tNombre " + p.deportista.nombre)
        print("\tAltura " + str(p.deportista.altura) + " Centimetros")
        print("\tPeso " + str(p.deportista.peso) + " Kilogramos")
        print("\tEdad " + str(p.edad))
        print("\tEquipo " + p.equipo.nombre)
        print("\tMedalla " + p.medalla)

    session.close_all()


def modificarMedalla():
    nombre = input("Escribe el nombre completo/parcial del deportista")

    sesionSQLLite = sqlLite()

    deportistas = sesionSQLLite.query(Deportista).filter(Deportista.nombre.contains(nombre))
    deportistaTotal = 0

    for d in deportistas:
        deportistaTotal += 1
        print(str(deportistaTotal) + "." + d.nombre)

    while True:

        eleccion = input("Indica con un numero que deportista Quieres selecionar")

        if int(eleccion) <= deportistaTotal:
            deportista = deportistas.offset(int(eleccion)-1).limit(1).one()
            break

    totalParticipaciones = 0

    for p in deportista.participaciones:
        totalParticipaciones += 1
        print(str(totalParticipaciones) + "." + p.evento.nombre + " Medalla: " + p.medalla)

    finalizar = True

    while finalizar:

        eleccion = input("Indica con un numero que participacion quieres modificar")

        if int(eleccion) <= deportistaTotal:

            participaciones = deportista.participaciones

            medalla = input("Elige por que medalla deseas editar"
                            "\n1.oro\n2.Plata\n3.Bronce\n4.N/A")
            while True:
                if int(medalla) == 1:
                    medalla = "oro"
                    finalizar = False
                    participaciones[int(eleccion) - 1].medalla = medalla
                    break

                elif int(medalla) == 2:
                    medalla = "plata"
                    finalizar = False
                    participaciones[int(eleccion) - 1].medalla = medalla
                    break

                elif int(medalla) == 3:
                    medalla = "bronce"
                    finalizar = False
                    participaciones[int(eleccion) - 1].medalla = medalla
                    break

                elif int(medalla) == 4:
                    medalla = "N/A"
                    finalizar = False
                    participaciones[int(eleccion) - 1].medalla = medalla
                    break


    # Ahora la editamos en MySQL

    sesionSQL = sql()

    deportista = sesionSQL.query(Deportista).filter(Deportista.id_deportista == deportista.id_deportista).one()
    participaciones = deportista.participaciones
    participacion = participaciones[int(eleccion) - 1]
    participacion.medalla = medalla

    sesionSQLLite.commit()
    sesionSQL.commit()

    sesionSQL.close()
    sesionSQLLite.close()


# No me ha dado tiempo de hacer este punto para poder enviartelo unos dias antes
def anadirDeportistaParticipacion():
    sesionSQLLite = sqlLite()

    nombre = input("Introduce el del deportista para crearlo o añadir una participacion")

    deportistas = sesionSQLLite.query(Deportista).filter(Deportista.nombre.contains(nombre))

    if (deportistas.count() == 0):
        print("El deportista con nombre " + nombre)

        print("Elige el sexo del deportista")
        print("1.M\n2.F")


    else:
        deportistaTotal = 0

        for d in deportistas:
            deportistaTotal += 1
            print(str(deportistaTotal) + "." + d.nombre)

        while True:

            eleccion = input("Indica con un numero que deportista Quieres selecionar")

            if int(eleccion) <= deportistaTotal:
                deportista = deportistas.offset(int(eleccion) - 1).limit(1).one()
                break

    while True:
        print("1. SQL")
        print("1. SQLLITE")

        elecion = input("Elige una de las dos opciones con los numeros 1 y 2")

        if elecion == "1":
            session = sql()
            break

        if elecion == "2":
            session = sqlLite()
            break

    # Ahora le preguntamos que temporada quiere
    while True:
        print("1. Winter")
        print("2. Summer")

        elecion = input("Porfavor elige una opcion escribiendo 1 o 2")

        if elecion == "1":
            temporada = "Winter"
            break

        if elecion == "2":
            temporada = "Summer"
            break

    listaOlipiadas = sesionSQLLite.query(Olimpiada).filter(Olimpiada.temporada == temporada)
    OlimpiadasTotal = 0

    for o in listaOlipiadas:
        OlimpiadasTotal += 1
        print(str(deportistaTotal) + "." + o.nombre)

    while True:

        eleccion = input("Indica con un numero que olimpiada quieres selecionar")

        if int(eleccion) <= OlimpiadasTotal:
            olimpiada = listaOlipiadas.offset(int(eleccion)-1).limit(1).one()
            idDeportista = olimpiada.id_olimpiada
            break

def eliminarParticipacion():
    sesionSQLLite = sqlLite()
    eliminar = False

    nombre = input("Escribe el nombre completo/parcial del deportista")

    deportistas = sesionSQLLite.query(Deportista).filter(Deportista.nombre.contains(nombre))
    deportistaTotal = 0

    for d in deportistas:
        deportistaTotal += 1
        print(str(deportistaTotal) + "." + d.nombre)

    while True:

        eleccion = input("Indica con un numero que deportista Quieres selecionar")

        if int(eleccion) <= deportistaTotal:
            deportista = deportistas.offset(int(eleccion)-1).limit(1).one()
            idDeportista = deportista.id_deportista
            break

    participacionTotal = 0

    for p in deportista.participaciones:
        participacionTotal += 1
        print(str(participacionTotal) + "." + p.evento.nombre)

    while True:

        eleccionParticipacion = input("Indica con un numero que evento quieres selecionar")

        if int(eleccionParticipacion) <= deportistaTotal:

            participaciones = deportista.participaciones

            participacion = participaciones[int(eleccionParticipacion) -1]

            sesionSQLLite.delete(participacion)
            sesionSQLLite.commit()

            deportista = sesionSQLLite.query(Deportista).filter(Deportista.id_deportista == deportista.id_deportista).one()

            participaciones = deportista.participaciones

            print(participaciones)

            if len(participaciones) == None:
                eliminar = True
                sesionSQLLite.delete(deportista)
            break

    # En MySQL
    # No se por que exactamente no esta borrando el deportista en ninguna de las bases de datos
    sesionSQL = sql()

    deportista = sesionSQL.query(Deportista).filter(Deportista.id_deportista == idDeportista).one
    participaciones = deportista.participaciones
    participacion = participaciones[int(eleccionParticipacion)-1]

    sesionSQL.delete(participacion)

    if eliminar == True:
        sesionSQL.delete(deportista)

    sesionSQL.commit()

    sesionSQL.close()
    sesionSQLLite.close()


def menu():
    finalizar = True

    while finalizar == True:
        print("""
        1.Listado de participantes
        2.Modificar medalla deportista
        3.Añadir deportista/participación
        4.Eliminar participación


        0.Salir
        """)

        opcion = int(input("Porfavor elige una opcion escribiendo un numero"))

        if opcion == 1:
            listarDeportistasParticipacion()

        if opcion == 2:
            modificarMedalla()

        if opcion == 3:
            anadirDeportistaParticipacion()

        if opcion == 4:
            eliminarParticipacion()

        if opcion == 0:
            finalizar = False


if __name__ == '__main__':
    anadirDeportistaParticipacion()