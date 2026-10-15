
# Ejercicio 3: Intentos limitados de inicio de sesión

clave_correcta = "1234"
intentos = 0
maximo_intentos = 3
acceso_concedido = False

while intentos < maximo_intentos:
    clave = input("Ingrese su contraseña: ")
    intentos += 1

    if clave == clave_correcta:
        acceso_concedido = True
        break
    else:
        print("Contraseña incorrecta.")

        if intentos < maximo_intentos:
            print("Intentos restantes:", maximo_intentos - intentos)

if acceso_concedido:
    print("Acceso permitido.")
else:
    print("Cuenta bloqueada.")
