class Juego:
    def __init__(self, numeroDeVidas):
        self.vidasIniciales = numeroDeVidas
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
        print("Record actual:", self.record)

    def quitaVida(self):
        self.numeroDeVidas = self.numeroDeVidas - 1
        if self.numeroDeVidas > 0:
            print("Te quedan", self.numeroDeVidas, "vidas")
            return True
        else:
            print("No te quedan más vidas")
            return False
