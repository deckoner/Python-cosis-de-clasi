from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine


# Crea un motor de base de datos específico para SQLite
DATABASE_URL = "mysql+pymysql://ex2:adat@172.20.132.130/examen2"
engine = create_engine(DATABASE_URL)


# Crea un objeto Base para declarar las entidades de la base de datos
Base = declarative_base()


class Alumnos(Base):
    __tablename__ = 'alumnos'
    DNI = Column(String, primary_key=True)
    APENOM = Column(String)
    POBLA = Column(String)
    TELEF = Column(String)
    NOTAS = relationship("Notas", back_populates="ALUMNO")


class Notas(Base):
    __tablename__ = 'notas'
    DNI = Column(String, ForeignKey('alumnos.DNI'), primary_key=True)
    COD = Column(Integer, ForeignKey('asignaturas.COD'), primary_key=True)
    NOTA = Column(Integer)
    ALUMNO = relationship("Alumnos", back_populates='NOTAS')
    ASIGNATURA = relationship("Asignaturas", back_populates='NOTA')


class Asignaturas(Base):
    __tablename__ = 'asignaturas'
    COD = Column(Integer, primary_key=True)
    NOMBRE = Column(String)
    ABREVIATURA = Column(String)
    NOTA = relationship("Notas", back_populates='ASIGNATURA')


# Crea un objeto session para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def listarAlumnos():
    db = SessionLocal()
    alumnos = db.query(Alumnos).all()

    for alumno in alumnos:
        print(alumno.APENOM)
        print("--------------------------")
        for nota in alumno.NOTAS:
            print(str(nota.ASIGNATURA.ABREVIATURA) + "\t\t" + str(nota.NOTA))
        print("")
    db.close()

def cambiarNombreAlumno():
    dni = input("Introduce el DNI del alumno")

    db = SessionLocal()
    alumno = db.query(Alumnos).filter(Alumnos.DNI == dni).first()

    if alumno == None:
        print("Ese alumno no existe en la base de datos")
    else:

        nombre = input("Escribe el nuevo nombre del alumno")

        if nombre == "":
            print("Se ha cancelado la operacion al no escribir un nombre nuevo")

        else:
            alumno.APENOM = nombre
            db.commit()
            db.close()


def cambiarNota():
    dni = input("Introduce el DNI del alumno")

    db = SessionLocal()
    alumno = db.query(Alumnos).filter(Alumnos.DNI == dni).first()

    if alumno == None:
        print("Ese alumno no existe en la base de datos")

    else:
        totalIndice = listarAsignaturas()

        while True:
            eleccion = input("Seleciona una de las opciones")

            if int(eleccion) <= totalIndice:
                nota = db.query(Notas).filter(Notas.COD == eleccion, Notas.DNI == dni).first()

                if nota == None:
                    crearNota(dni, eleccion)
                else:
                    editarNota(dni, eleccion)

                break


def crearNota(dni, cod):
    puntuacion = input("Indica la puntuacion de la nota")

    nota = Notas(DNI=dni, COD=cod, NOTA=puntuacion)
    db = SessionLocal()
    db.add(nota)
    db.commit()
    db.close()

    print("Se ha creado una nueva nota para el alumno")


def editarNota(dni, cod):
    puntuacion = input("Indica la puntuacion de la nota")

    db = SessionLocal()
    nota = db.query(Notas).filter(Notas.DNI == dni, Notas.COD == cod).first()
    nota.NOTA = puntuacion
    db.commit()
    db.close()

    print("Se ha editado la nota para el alumno")


def listarAsignaturas():
    db = SessionLocal()
    asignaturas = db.query(Asignaturas).all()

    total = 0
    for asignatura in asignaturas:
        total += 1
        print(str(total) + "-." + asignatura.NOMBRE + " (" + asignatura.ABREVIATURA + ")")

    return total