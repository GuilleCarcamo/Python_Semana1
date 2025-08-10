#Desafío 1 — Minutos a hh:mm
#Objetivo: ingresar una cantidad de minutos y convertir a formato HH:MM (cero a la izquierda).

min = int(input("Ingrese cantidad en minutos: "))
horas = min // 60
mins = min % 60

print(f"{horas:02d}: {mins:02d}")

