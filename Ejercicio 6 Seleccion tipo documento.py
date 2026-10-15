# Ejercicio 6: Selección de tipo de documento

tipos_validos = ("CC", "TI", "CE")

while True:
    tipo_documento = input(
        "Ingresa el tipo de documento (CC, TI o CE): "
    ).strip().upper()

    if tipo_documento in tipos_validos:
        print(f"El tipo de documento ingresado fue : {tipo_documento} Tenga un buen dia")
        break
    else:
        print("Error: Recuerda que solo se permite CC, TI o CE.")