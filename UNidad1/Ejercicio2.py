from statistics import mean

if __name__ == '__main__':

    listaNumeros = []

    for n in range(3):
        listaNumeros.append(int(input("Porfavor introduzca un numero")))

    print(listaNumeros)

    print(sum(listaNumeros))
    print(mean(listaNumeros))


