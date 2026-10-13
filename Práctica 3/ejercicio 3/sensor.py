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
