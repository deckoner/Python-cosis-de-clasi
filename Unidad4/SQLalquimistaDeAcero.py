from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Unidad4.Model.Mapeo import *

engine = create_engine("sqlite:///enbebido.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# resultado = session.query(Participacion).all()
#
# for d in resultado:
#     print(d.id_deportista, " ",  d.id_evento, " ", d.id_equipo, " ", d.edad, " ", d.medalla)
#

resultado = session.query(Evento).all()

for e in resultado:
    print(e.deporte.nombre)