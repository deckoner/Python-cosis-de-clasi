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

    print(listaNumeros)
    print(sum(listaNumeros))
    print(mean(listaNumeros))