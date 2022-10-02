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

def copiar():
    rutaDelArchivo = input("Introduce la ruta del archivo a copiar")

    if (os.path.exists(rutaDelArchivo) == True):
        rutaDestino = input("Introduce la ruta donde se copiara el archivo")

        if (os.path.exists(rutaDestino) == True):
            shutil.copy(rutaDelArchivo, rutaDestino)
            print("Se a copiado el archivo con exito")

        else:
            print("La direccion de destino no existe")

    else:
        print("El archivo no existe o has escrito mal su nombre")

def moverArchivo():
    rutaDelArchivo = input("Introduce la ruta del archivo a copiar")

    if (os.path.exists(rutaDelArchivo) == True):
        rutaDestino = input("Introduce la ruta donde se movera el archivo")

        if (os.path.exists(rutaDestino) == True):
            shutil.move(rutaDelArchivo, rutaDestino)
            print("Se a movido el archivo con exito")

        else:
            print("La direccion de destino no existe")

    else:
        print("El archivo no existe o has escrito mal su nombre")

def eliminarArchiDirectorio():
    ruta = input("Introduce la ruta del archivo/directorio a eliminar")

    if (os.path.exists(ruta) == True):

        if (os.path.isfile(ruta) == True):

            os.path.remove(ruta)
            print("El archivo se elimino correctamente")

        else:
            try:
                os.rmdir(ruta)
                print("El directorio ha sido eliminado")

            except:
                print("Para eliminar el directorio debe de estar vacio")

    else:
        print("El archivo/directorio no existe")


if __name__ == '__main__':

    finalizar = True

    while finalizar == True:
        print("""
        1. Crear directorio
        2.Listar un directorio
        3.Copiar un archivo
        4.Mover un archivo
        5.Eliminar un archivo/directorio
        6.Salir
        """)

        n = int(input("Elige una de las opciones con un numero"))

        if(n == 1):
            crearDirectorio()

        if(n == 2):
            listarDirectorios()

        if(n == 3):
            copiar()

        if(n == 4):
            moverArchivo()

        if(n == 5):
            eliminarArchiDirectorio()

        if(n == 6):
            finalizar = False