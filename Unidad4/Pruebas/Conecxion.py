from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///endebido.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
session.execute('pragma foreign_Keys=on')

# Añadir alumno
# a = Alumno(nombre="Mikel")
# session.add(a)
# session.commit()
# session.close()

# Añadir Nota
# n = Nota(id_alumno=10, modulo="ADAT", nota="5")
# session.add(n)
# session.commit()
# session.close()

# n = session.query(Nota).filter(Nota.id_alumno==1).one()
# session.delete(n)
# session.commit()
# session.close()