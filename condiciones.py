opcion = 0   # valor inicial, solo para entrar al while

while opcion != 2:
    print("Bienvenido, escoja una opcion:")
    print("1. saber rango edad")
    print("2. salir")
    opcion = int(input("Opción: "))

    if opcion == 1:
        edad = int(input("Dame tu edad: "))

        if edad >= 18 and edad < 45:
            print("Eres adolescente")
        elif edad < 18:
            print("Eres niño")
        elif edad >= 45 and edad < 60:
            print("Eres adulto")
        else:
            print("Eres adulto mayor")

    elif opcion == 2:
        print("Saliendo...")
    else:
        print("Opción no válida, intenta de nuevo.")