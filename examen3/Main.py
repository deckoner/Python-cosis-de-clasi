from examen3.Mapeo import *

while True:
    print("1. Ejercicio 2")
    print("2. Ejercicio 3")
    print("3. Ejercicio 4")
    print("0. salir")

    eleccion = int(input("Elige con un numero cual quieres"))

    if eleccion == 1:
        listarAlumnos()
        break

    if eleccion == 2:
        cambiarNombreAlumno()
        break

    if eleccion == 3:
        cambiarNota()
        break

    if eleccion == 0:
        break