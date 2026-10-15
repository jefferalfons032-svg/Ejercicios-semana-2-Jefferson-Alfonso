# Ejercicio 11: Factorial de un número

while True:
    try:
        numero = int(input("Ingrese un numero entero (No tiene que ser negativo): "))

        if numero >= 0:
            break

        print("Error: Por favor el numero no puede ser negativo.")

    except ValueError:
        print("Error: debe ingresar un número entero.")

factorial = 1

for valor in range(1, numero + 1):
    factorial *= valor

print(f"El factorial de {numero} es: {factorial}")