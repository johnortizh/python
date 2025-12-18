
"""
persona = {
    "nombre": "john",
    "edad": 34,
    "ciudad": "Bogota"
}

print(f"Hola {persona.get("nombre")}, su edad es de: {persona.get("edad")}")

persona["edad"] = 35
persona["profesion"] = "ingeniero"
print(f"la edad cambio a: {persona.get("edad")}")
print(f"su profesion es: {persona.get("profesion")}")

for clave, valor in persona.items():
    print(f"{clave}:{valor}")

"""
datos = {
    "nombre": "john",
    "email": "johnortizh@outlook.com",
    "direccion": {
        "ciudad": "Bogota",
        "pais": "Colombia"
    }
}

print(f"la ciudad es: {datos.get('direccion').get('ciudad')}")
print(f"el pais es: {datos.get('direccion').get('pais')}")