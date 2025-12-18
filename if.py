"""
📝 Ejercicio 3 — Mini reto (realista)
Pide:
edad
salario mensual
Reglas:
Si edad < 18 → “No elegible”
Si salario < 1000 → “Salario bajo”
Si salario entre 1000 y 3000 → “Salario medio”
Si salario > 3000 → “Salario alto”

print("Ejercicio 1")
numero = int(input("Dame un numero: "))
if numero > 0:
    print("el numero es positivo")
elif numero == 0:
    print("el numero es cero")
elif numero < 0:
    print("el numero es negativo")    



print("Ejercicio 2")
user = "admin"
password = "1234"
usuario = input("Digite su usuario: ")
contraseña = input("Digite su contraseña: ")
if usuario == user and password == contraseña:
    print("Acceso permitido")
else:
    print("Acceso denegado")    
    

print("Ejercicio 3")
edad = int(input("Cual es tu edad: "))

"""

salarios = [900, 1200, 2500, 800, 3200]

cantidad = 0 
for salario in salarios:
    if salario > 1000:
        cantidad+=1

print(f"cantidad de salarios mayor a 1000: {cantidad}")