class criptografo():

    def encriptar(self, cadena):
        i = 0
        tamano = len(cadena)
        temp = ""
        cadenaCodificada = ""
        while i < tamano:

            temp = (ord(cadena[i]) + 1)
            cadenaCodificada += str(chr(temp))

            i += 1
        return cadenaCodificada

    def desencriptar(self, cadena):
        i = 0
        tamano = len(cadena)
        temp = ""
        cadenaCodificada = ""
        while i < tamano:

            temp = (ord(cadena[i]) - 1)
            cadenaCodificada += str(chr(temp))

            i += 1
        return cadenaCodificada

if __name__ == '__main__':

    str1 = "Gatete lindo"

    crip = criptografo()

    str1 =crip.encriptar(str1)

    print(str1)

    print(crip.desencriptar(str1))