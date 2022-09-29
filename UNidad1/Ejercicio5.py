from statistics import mean

def sumatorio(lista):
    return sum(lista)

def media(lista):
    return mean(lista)

def maximo(lista):
    return (max(lista))

def minimo(lista):
    return (min(lista))


if __name__ == '__main__':

    listaNumeros = []
    finalizar = False

    for n in range(3):

        while True:
            numero = int(input("Porfavor introduzca un numero"))

            if (numero % 2) == 0:
                pass
            else:
                listaNumeros.append(numero)
                break

    while finalizar == False:
        print("""
        ¿Que desea hacer con lal ista?
            1. Sumatorio
            2. Media
            3. Maximo
            4. Minimo
            0. Salit
        """)

        eleccion = int(input("Elige una opcion solo escrbiendo el numero porfavor"))

        if eleccion == 1:
            print(sumatorio(listaNumeros))
            finalizar = True

        if eleccion == 2:
            print(media(listaNumeros))
            finalizar = True

        if eleccion == 3:
            print(maximo(listaNumeros))
            finalizar = True

        if eleccion == 4:
            print(minimo(listaNumeros))
            finalizar = True

        if eleccion == 0:
            finalizar = True
