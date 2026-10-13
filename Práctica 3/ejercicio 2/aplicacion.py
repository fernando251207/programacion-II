from juego_adivina_numero import JuegoAdivinaNumero
from juego_adivina_par import JuegoAdivinaPar
from juego_adivina_impar import JuegoAdivinaImpar

juego1 = JuegoAdivinaNumero(3)
juego2 = JuegoAdivinaPar(3)
juego3 = JuegoAdivinaImpar(3)

print("--- Juego normal ---")
juego1.juega()
print("--- Juego de pares ---")
juego2.juega()
print("--- Juego de impares ---")
juego3.juega()
