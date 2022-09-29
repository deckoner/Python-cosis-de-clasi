from statistics import mean

if __name__ == '__main__':

    listaNumeros = []

    for n in range(3):

        while True:
            numero = int(input("Porfavor introduzca un numero"))

            if (numero % 2) == 0:
                pass
            else:
                listaNumeros.append(numero)
                break

    while True:
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
            print(sum(listaNumeros))
            break

        if eleccion == 2:
            print(mean(listaNumeros))
            break

        if eleccion == 3:
            print(max(listaNumeros))
            break

        if eleccion == 4:
            print(min(listaNumeros))
            break

        if eleccion == 0:
            break