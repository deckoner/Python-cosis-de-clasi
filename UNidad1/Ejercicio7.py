import random


class persona():

    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__dni = self.generarDNI()
        self.__sexo = "H"
        self.__peso = 0
        self.__altura = 0

    def calcularIMC(self):
        imc = self.peso / self.altura**2

        if (imc >= 25):
            return 1
        if (imc >= 20):
            return 0
        else:
            return -1

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def toString(self):
        return "Nombre: " + self.nombre + " edad: " + self.edad + " DNI: " + self.dni + " sexo: " + self.sexo + "peso" \
                                                                            ": " + self.peso + " altura: " + self.actura

    def generarDNI(self):
        numeroAleatorio = random.randint(10000000, 99999999)
        return numeroAleatorio
