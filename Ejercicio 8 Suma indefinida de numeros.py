# Ejercicio 8: Suma indefinida de números

suma = 0
numero = 1

while numero != 0:
    numero = int(input("Ingrese un numero (0 para terminar): "))
    suma = suma + numero

print("La suma total es:", suma)