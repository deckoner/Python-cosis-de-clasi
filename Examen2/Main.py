from Examen2.sql import *


def notasAlumnos():
    ListaAlumnos = notaDeAlumnos()

    AnteriorNombre = ListaAlumnos[0][0]

    print(AnteriorNombre+
          "\n---------------------------------")

    for alumno in ListaAlumnos:
        if alumno[0] == AnteriorNombre:
            print(alumno[1] + "\t\t" + str(alumno[2]))
        else:
            print("\n" +alumno[0]+
                  "\n---------------------------------")
            print(alumno[1] + "\t\t" + str(alumno[2]))
            alumno[0] == AnteriorNombre


def cambiarNombreAlumno():

    while True:
        try:
            dni = input("Escribe el DNI del alumno del que deseas modificar")
            if len(dni) == 8:
                break

        except:
            print("El DNI tiene que ser todo numeros y sin letra")

    if existeNombreAlumno(dni):
        print(mostrarNombreAlumno(dni)[0])
        nombre = input("Introduzca el nombre por el que quieres cambiarlo")

        if nombre == "":
            cambiarNombre(dni, nombre)
            print("Se ha cambiado correctamente el nombre del alumno")
    else:
        print("No ahi ningun alumno con ese DNI")


def cambiarNotaAlumno():
    while True:
        try:
            dni = input("Escribe el DNI del alumno del que deseas modificar")
            if len(dni) == 8:
                break

        except:
            print("El DNI tiene que ser todo numeros y sin letra")

    if existeNombreAlumno(dni):
        print(mostrarNombreAlumno(dni)[0])

        listaAsignaturas = listarAsignaturas()

        print("Listado de asignaturas disponibles")
        for asignatura in listaAsignaturas:
            print(str(asignatura[0]) + "- " + asignatura[1] + " (" + asignatura[2] + ")")

        while True:
            codigo = int(input("Escribe el codigo de la asignatura a evaluar"))-1

            if (codigo <= len(listaAsignaturas)):
                nota = input("Escribe la nota del alumno")
                break

        if existeClasificacion(listaAsignaturas[codigo][0], dni):
            actualizarNota(nota, listaAsignaturas[codigo][0], dni)
            print("La nota se ha añadido")


        else:
            crearNota(dni, listaAsignaturas[codigo][0], nota)
            print("La nota se ha modificado")

    else:
        print("No ahi ningun alumno con ese DNI")


if __name__ == '__main__':
    notasAlumnos()