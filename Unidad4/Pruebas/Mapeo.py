from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

# Crea un motor de base de datos específico para SQLite
DATABASE_URL = "sqlite:///alumnos.db"
engine = create_engine(DATABASE_URL)

# Crea un objeto Base para declarar las entidades de la base de datos
Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    notas = relationship("Nota", back_populates="alumno")

class Nota(Base):
    __tablename__ = 'nota'
    id = Column(Integer, primary_key=True)
    alumno_id = Column(Integer, ForeignKey('alumno.id'))
    modulo = Column(String)
    nota = Column(Integer)
    alumno = relationship("Alumno", back_populates='notas')
 
# Crea un objeto session para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para crear un alumno
def create_alumno(nombre):
    alumno = Alumno(nombre=nombre)
    db = SessionLocal()
    db.add(alumno)
    db.commit()
    db.close()
 
# Función para crear una nota
def create_nota(alumno_id, modulo, nota):
    nota = Nota(alumno_id=alumno_id, modulo=modulo, nota=nota)
    db = SessionLocal()
    db.add(nota)
    db.commit()
    db.close()

# Función para actualizar una nota dado su id
def update_nota(nota_id, modulo, nota):
    db = SessionLocal()
    nota = db.query(Nota).filter(Nota.id == nota_id).first()
    nota.modulo = modulo
    nota.nota = nota
    db.commit()
    db.close()

# Función para actualizar un alumno dado su id
def update_alumno(alumno_id, nombre):
    db = SessionLocal()
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()
    alumno.nombre = nombre
    db.commit()
    db.close()
    
# Función para listar todos los alumnos con sus respectivas notas
def list_alumnos_notas():
    db = SessionLocal()
    alumnos = db.query(Alumno).options(joinedload(Alumno.notas)).all()
    for alumno in alumnos:
        print(alumno.nombre)
        for nota in alumno.notas:
        print(f'{nota.modulo} - {nota.nota}')
    db.close()

# Función para listar todas las notas de un alumno dado su id
def list_notas_alumno(alumno_id):
    db = SessionLocal()
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()
    if alumno:
        print(alumno.nombre)
        for nota in alumno.notas:
            print(f'{nota.modulo} - {nota.nota}')
    else:
        print(f'No existe el alumno con id {alumno_id}')
    db.close()

# Función para eliminar una nota dado su id
def delete_nota(nota_id):
    db = SessionLocal()
    nota = db.query(Nota).filter(Nota.id == nota_id).first()
    if nota:
        db.delete(nota)
        db.commit()
        print(f'Nota con id {nota_id} eliminada.')
    else:
        print(f'No existe una nota con id {nota_id}.')
    db.close()

# Función para eliminar un alumno dado su id
def delete_alumno(alumno_id):
    db = SessionLocal()
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()
    if alumno:
        db.delete(alumno)
        db.commit()
        print(f'Alumno con id {alumno_id} eliminado.')
    else:
        print(f'No existe un alumno con id {alumno_id}.')
        db.close()
