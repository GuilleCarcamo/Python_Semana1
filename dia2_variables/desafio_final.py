#Pedir dos números y mostrar:
#Suma
#Resta
#Multiplicación
#División (con 2 decimales)
#Todo usando f-strings.

num1 = float(input("Valor de num 1: "))
num2 = float(input("Valor de num 2: "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
print(f"Suma: {suma}, Resta: {resta}, Multiplicacion: {mult}, Division: {div:.2f}")