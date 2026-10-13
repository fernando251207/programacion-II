from camara import Camara
from sensor_luz_laser import SensorLuzLaser


class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehículo Autónomo"

    def __init__(self, id, resolucion, alcance):
        Camara.__init__(self, id, resolucion)
        SensorLuzLaser.__init__(self, id, alcance)
