


personas = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Luis", "edad": 31},
    {"nombre": "Pedro", "edad": 19},
]

for persona in personas:
    nombre = persona["nombre"]
    print(nombre)


"""


numero = int(input("dame un numero: "))

for indice in range(1,11):
    print(f"{numero} * {indice} = {numero * indice}")



numero = 3

for i in range(20):
    print(i)
    if i == numero:
        print(f"numero encontrado {i}")
        break


numeros = [4, 7, 1, 8, 3]
suma=0

for i in numeros:
    suma += i


print(f"la siuma d elos umeros es: {suma}")


palabra = input("dame una palabra: ")
vocales = "aeiou"
contador = 0

for i in palabra:
    if i in vocales:
        contador += 1

print(f"la cantidad de vocales son: {contador}")


for caracter in palabra:
    print(caracter)
"""