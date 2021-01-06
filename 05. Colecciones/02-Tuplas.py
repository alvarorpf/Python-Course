# Uso de tuplas en python
# Una tupla es similar a una lista solo que esta no puede ser modificada
# La creacion de una tupla se emplea los parentesis en lugar de los corchetes que se emplean en las listas

frutas = ("Naranja", "Platano", "Manzana")
print(frutas)

# Se pueden utilizar los mismos comandos de una lista dentro de una tupla
# Tamaño de una tupla
print(len(frutas))

# Acceder a un elemento de una tupla mediante un indice
print(frutas[0])
print(frutas[1])
print(frutas[2])

# Navegacion Inversa 
print(frutas[-1])

# Uso de rangos
print(frutas[0:2])
print(frutas[1:])
print(frutas[:2])

# Se puede modificar una tupla cambiando la tupla a una lista y volviendola una tupla nuevamente
# Para realizar la conversion se emplean los comandos list() y tuple()
frutasLista = list(frutas)
frutasLista[1] = "Sandia"
frutas = tuple(frutasLista)
print(frutas)

# Iteracion de una lista
# En la funcion print se puede utilizar el comando end= para poder imprimir en una misma linea todos los valores
for fruta in frutas:
    print(fruta, end=" ")

# No se pueden agregar ni modificar los elementos de una tupla pero se puede eliminar el valor de esta variable con el comando del
del frutas