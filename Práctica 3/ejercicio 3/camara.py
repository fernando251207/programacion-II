from sensor import Sensor


class Camara(Sensor):
    tipo = "Cámara"

    def __init__(self, id, resolucion):
        Sensor.__init__(self, id)
        self.resolucion = resolucion
