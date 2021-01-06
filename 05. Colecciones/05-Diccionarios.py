# Uso de colecciones de tipo diccionario en python
# Los diccionarios contienen la siguiente estructura 
# Contienen una llave o key con un valor asociado a la misma (Moto = "Honda")
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}
print(diccionario)

# Tamaño del diccionario
print(len(diccionario))

# Para acceder a un valor de un diccionario se emplean las llaves del mismo
print(diccionario["IDE"])

# Otra forma de obtener un valor es utilizando la funcion get
print(diccionario.get("OOP"))

# Se pueden modificar los valores de un diccionario
diccionario["IDE"] = "Integrated development environment"
print(diccionario)

# Iteracion de elementos de un diccionario
# Obtencion de las llaves del diccionario
for llave in diccionario:
    print(llave)

# Obtencion de los valores del diccionario mediante las llaves    
for llave in diccionario:
    print(diccionario[llave])

# Obtencions de los valores del diccionario mediante la funcion values    
for valor in diccionario.values():
    print(valor)

# Comprobacion de existencia de una llave dentro de un diccionario
print("IDE" in diccionario)

# Agregar elementos a un diccionario
diccionario["PK"] = "Primary Key"
print(diccionario)

# Remover elementos de un diccionario
diccionario.pop("DBMS")
print(diccionario)

# Limpiar los elementos de un diccionario 
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario