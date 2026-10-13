from vehiculo_autonomo import VehiculoAutonomo
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
