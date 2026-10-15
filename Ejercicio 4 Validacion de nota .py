# Ejercicio 4: Validación de nota

nota = -1

while nota < 0 or nota > 5:
    nota = float(input("Ingresa la nota entre 0.0 y 5.0: "))

    if nota < 0 or nota > 5:
        print("Error, Recuerda que la nota debe estar entre 0.0 y 5.0")

print("La nota fue registrada correctamente :D:", nota)