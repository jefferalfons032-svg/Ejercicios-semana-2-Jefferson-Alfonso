
# Ejercicio 1: Menú principal de un sistema

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar")
    print("2. Registrar")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Ha seleccionado la opción Consultar.")

    elif opcion == 2:
        print("Ha seleccionado la opción Registrar.")

    elif opcion == 3:
        print("Saliendo del sistema, hasta pronto.")
        break

    else:
        print("Opción inválida. Seleccione 1, 2 o 3.")
