class Sensor:
    
    tipo = "Genérico"

    def __init__(self, id):
        self.id = id
        self.encendido = False

    def activar(self):
        self.encendido = True
        print(f"Sensor {self.id} activado")

    def desactivar(self):
        self.encendido = False
        print(f"Sensor {self.id} desactivado")


class Camara(Sensor):
   
    tipo = "Cámara"

    def __init__(self, id, resolucion):
        Sensor.__init__(self, id)
        self.resolucion = resolucion


class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"

    def __init__(self, id, alcance):
        Sensor.__init__(self, id)
        self.alcance = alcance


class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehículo Autónomo"

    def __init__(self, id, resolucion, alcance):
        Camara.__init__(self, id, resolucion)
        SensorLuzLaser.__init__(self, id, alcance)


auto = VehiculoAutonomo("VA-01", "1920x1080", 150)

print("Tipo:", auto.tipo)
print("ID:", auto.id)
print("Resolución:", auto.resolucion)
print("Alcance:", auto.alcance)
print("Encendido:", auto.encendido)

auto.activar()
print("Encendido:", auto.encendido)

auto.desactivar()
print("Encendido:", auto.encendido)