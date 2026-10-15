
# Ejercicio 2: Validación de clave fija

clave_correcta = "1234"

while True:
    clave = input("Ingrese su contraseña numérica: ")

    if clave == clave_correcta:
        print("Bienvenido al sistema.")
        break
    else:
        print("Contraseña incorrecta. Intente nuevamente.")
