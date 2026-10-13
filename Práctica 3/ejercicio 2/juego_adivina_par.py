from juego_adivina_numero import JuegoAdivinaNumero


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero % 2 == 0 and numero >= 0 and numero <= 10:
            return True
        if numero % 2 != 0:
            print("Error: el número debe ser par")
        return False
