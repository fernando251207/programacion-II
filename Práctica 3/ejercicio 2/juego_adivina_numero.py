import random
from juego import Juego


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        Juego.__init__(self, numeroDeVidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            return True
        else:
            return False

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")
        seguir = True
        while seguir:
            numero = int(input("Ingresa un número: "))
            if not self.validaNumero(numero):
                print("Número no válido, intenta de nuevo")
            elif numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                seguir = False
            else:
                if self.quitaVida():
                    if self.numeroAAdivinar > numero:
                        print("El número a adivinar es mayor")
                    else:
                        print("El número a adivinar es menor")
                else:
                    print("El número era:", self.numeroAAdivinar)
                    seguir = False
