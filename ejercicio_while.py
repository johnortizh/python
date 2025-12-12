lista_menu = ["\nBienvenido", "1. mostrar lista nombres", "2. agregar nombre", "3. eliminar nombre", "4. salir"]
lista_nombre = []
opcion = 0

while opcion != 4:
    for i in lista_menu:
        print(i)
    
    opcion=int(input("escoja una opcion: "))

    if opcion == 1:
        print("\nLista de nombres\n")
        for lista in lista_nombre:
            print(lista)
    elif opcion == 2:
        nombre = input("escriba el nombre a ingresar: ")
        lista_nombre.append(nombre)
        print("\n!! nombre agregado !!")
    elif opcion == 3:
        nombre = input("escriba el nombre a eliminar: ")
        lista_nombre.remove(nombre)
        print("\n !! nombre eliminado !!")