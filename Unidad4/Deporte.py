import SQLalquimistaDeAcero as db

from sqlalchemy import Column, Integer, String, Float

class Producto(db.Base):
    __tablename__ = 'deporte'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'Producto({self.nombre})'

    def __str__(self):
        return self.nombre