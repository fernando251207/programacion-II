from sensor import Sensor


class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"

    def __init__(self, id, alcance):
        Sensor.__init__(self, id)
        self.alcance = alcance
