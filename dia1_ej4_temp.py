#Ejercicio 4 — Conversión de temperatura
#Objetivo: convertir °C a °F con fórmula F = C * 9/5 + 32.
#Formato: XX.X C -> YY.Y F (redondeá a 1 decimal).

C = float(input("Temperatura en C°: "))
F = C * 9/5 + 32
print(f"{C:.1f}. C - > {F:.1f} F")