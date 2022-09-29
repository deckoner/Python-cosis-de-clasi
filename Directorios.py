import os
import shutil

def crearDirectorio():

    ruta = input("Indique la ruta donde se creara el directorio")
    nombre = input("Indique el nombre del directorio que desea crear")

    try:
        os.mkdir(ruta + "/" + nombre)
    except OSError as e:
        print("Lo sentimos pero esa carpeta ya existe")

def listarDirectorios():
    ruta = input("Intoduce la ruta del directorio a listar")

    lista = os.listdir(ruta)

    for n in lista:
        if (os.path.isdir(os.path.join(ruta + "/" + n))):
            print("Esto es una carpeta: " + n)
        if (os.path.isfile(os.path.join(ruta + "/" + n))):
            print("Esto es una fichero: " + n)

if __name__ == '__main__':

    finalizar = True

    while finalizar == True:
        print("""1. Crear directorio
        2.Listar un directorio
        3.Copiar un archivo
        4.Mover un archivo
        5.Eliminar un archivo/directorio
        6.Salir
        """)

        n = int(input("Elige una de las opciones con un numero"))

        if(n == 1):
            crearDirectorio()
            finalizar = False

        if(n == 2):
            listarDirectorios()
            finalizar = False

        if(n == 3):
            pass

        if(n == 4):
            pass

        if(n == 5):
            pass

        if(n == 6):
            pass