from Unidad4.Pruebas.Mapeo import list_alumnos_notas

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

list_alumnos_notas()