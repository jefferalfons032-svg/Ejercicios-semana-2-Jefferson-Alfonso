# Ejercicio 14: Serie de Fibonacci

cantidad = int(input("Ingrese la cantidad de los terminos por favor : "))

a = 0
b = 1

for i in range(cantidad):
    print(a, end=" ")
    siguiente = a + b
    a = b
    b = siguiente