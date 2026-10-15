# Ejercicio 10: Calculadora de promedios

suma = 0
cantidad = 0

nota = float(input("Ingrese una nota ( -1 para terminar): "))

while nota != -1:
    if nota >= 0 and nota <= 5:
        suma = suma + nota
        cantidad = cantidad + 1
    else:
        print("La nota debe estar entre 0 y 5.")

    nota = float(input("Ingrese otra nota (-1 para terminar): "))

if cantidad > 0:
    promedio = suma / cantidad
    print("El promedio es:", promedio)
else:
    print("No se ingresaron notas.")