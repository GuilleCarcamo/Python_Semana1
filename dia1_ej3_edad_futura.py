#Ejercicio 3 — Edad en un año futuro
#Objetivo: leer edad actual y un año futuro; calcular cuántos años tendrás.
#Asumí que estamos en 2025 (hoy es 10 de agosto de 2025).
#Formato: En <año> tendrás <edad> años


edad = int(input("Ingrese su edad: "))
anio_futuro = int(input("Ingrese un año a futuro: "))
anio_actual = 2025
edad_futuro = edad + (anio_futuro - anio_actual) 
print(f"En el año {anio_futuro}, usted tendra {edad_futuro} ")

