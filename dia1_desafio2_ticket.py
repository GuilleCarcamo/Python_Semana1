#Desafío 2 — Ticket simple
#Objetivo: pedir producto (str), precio (float), cantidad (int).
#Calcular total y mostrar:
#Producto: <producto> | Unit: $X.XX | Cant: N | Total: $Y.YY

prod = str(input("Ingrese un producto: "))
precio = float(input("Ingrese un precio: "))
cant = int(input("Ingrese la cantidad: "))

total = cant * precio

print(f"Producto: {prod}, Unit: ${precio:.2f}, Cant: {cant}, Total: {total:.2f} ")