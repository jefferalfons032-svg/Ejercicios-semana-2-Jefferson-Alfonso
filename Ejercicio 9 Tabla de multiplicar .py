# Ejercicio 9: Tabla de multiplicar

while True:
    try:
        numero = int(input("Ingrese un numero entero por favor :D : "))
        break
    except ValueError:
        print("Error: Por favor ingrese un numero entero .")

print(f"\nTabla de multiplicar del {numero}")

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")