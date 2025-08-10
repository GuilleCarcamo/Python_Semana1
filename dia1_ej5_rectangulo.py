#Ejercicio 5 — Área y perímetro de rectángulo
#Objetivo: leer base y altura (floats) y mostrar área y perímetro.
#Formato: Area=AA.A Perimetro=PP.P (1 decimal).

B = float(input("Ingrese el valor de base: "))
A = float(input("Ingrese el valor de altura: "))
area = B * A
perimetro = 2 * (B + A)

print(f"Area={area:.1f}, Perimetro={perimetro:.1f}")

