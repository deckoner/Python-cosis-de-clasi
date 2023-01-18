from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'Alumno'
    id_alumno = Column(Integer, primary_key=True)
    nombre = Column(String)

class Nota(Base):
    __tablename__ = 'Nota'
    id_nota = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey('Alumno.id_alumno'))
    modulo = Column(String)
    nota = Column(Integer)
    alumno = relationship("Alumno", back_populates='notas')

Alumno.notas = relationship("Nota", back_populates="alumno")

