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
        print(e.nombre)

    while True:
        elecion = input("Seleciona escribiendo el numero del evento que quieres")

        if int(elecion) <= totalEvento:
            idEvento = eventoDiccionario[int(elecion)]
            break
            


def modificarMedalla():
    pass


def anadirDeportistaParticipacion():
    pass


def eliminarParticipacion():
    pass


def menu():
    pass


if __name__ == '__main__':
    listarDeportistasParticipacion()
