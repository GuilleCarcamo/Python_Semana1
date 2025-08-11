#Pedir el radio (float) y calcular:

import math

valor = float(input("Ingrese el valor de radio: "))
radio_cuadrado = valor ** 2 
print(f"Con radio {valor}, el área del círculo es {math.pi * radio_cuadrado:.2f}")
