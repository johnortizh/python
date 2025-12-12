frutas = ["manzana", "pera", "rambután", "salak"]
opcion = 0 
while opcion !=3:
    print("Bienvenido a la tienda de frutas.")
    print("1. Ver frutas disponibles")
    print("2. Agregar una fruta")
    print("3. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Frutas disponibles: ")
        for indice, fruta in enumerate(frutas, start=1):
            print(f"{indice}. {fruta}")
    elif opcion == 2:
        nueva_fruta = input("Ingresa el nombre de la fruta que deseas agregar: ")
        frutas.append(nueva_fruta)
        print("Fruta agregada. Frutas disponibles ahora son: ")
        for i in frutas:
            print(i)
    elif opcion == 3:
        print("Saliendo de la tienda. ¡Gracias por visitarnos!")