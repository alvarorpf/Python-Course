# Uso de listas en python
# Una lista es un conjunto de variables o datos

nombres = ["Alvaro", "Renato", "Andrea", "Carla"]
print(nombres)

# Comando para saber la cantidad de elementos de una lista
print (len(nombres))

# Para acceder a un elemento de la lista se suele utilizar el indice en el que se encuentra este elemento
# Se debe tener en cuenta que si se emplea un indice que este fuera de rango el interpretador de python devolvera un error
print(nombres[0])
print(nombres[1])
# Tambien se pueden utilizar los indices inversos para navegar entre los elementos de la lista
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango de elementos de una lista
# Se utiliza : para imprimir el numero de elementos que se desea obtener de la lista
print(nombres[0:2])

# Impresion de elementos desde el inicio hasta un elemento anterior
print(nombres[:3])

# Impresion de elementos desde el indice de inicio hasta el ultimo
print(nombres[1:])

# Cambio de elementos  de una lista
# Se selecciona el elemento de la lista mediante el uso de su indice y se le da un nuevo valor a esta
nombres[3] = "Lorena"
print(nombres)

# Se puede realizar la iteracion de una lista mediante el ciclo for
for nombre in nombres:
    print(nombre)
    
# Se puede buscar un elemento dentro de una lista con el condicional if y el comando in
if "Renato" in nombres:
    print ("Se encuentra en la lista")
else: 
    print("No se encuentra en la lista")
    
# Adicion de un nuevo elemento a la lista
# Para agregar un nuevo elemento se utiliza el comando append a continuacion del nombre de la lista
nombres.append("Juan")
print(nombres)

# Agregar un nuevo elemento en un indice especifico de la lista
# Para agregar un nuevo elemento en un indice especifico se utiliza el comando insert seguido del nombre de la lista
# Para realizar la insercion se debe indicar el indice y el valor del elemento
nombres.insert(1,"Luis")
print(nombres)

# Remover un elemento de la lista por el valor utilizando el comando remove
nombres.remove("Luis")
print(nombres)
# Se puede remover el ultimo elemento de una lista utilizando el comando pop
nombres.pop()
print(nombres)

# Se puede remover un elemento indicando el indice de un lista mediante el comando del
del nombres[0]
print(nombres)

# Para limpiar todos los elementos de una lista se utiliza el comando clear
nombres.clear()
print(nombres)

# Para eliminar por completo una variable se puede emplear el comando del 
# En caso de utilizar el comando del si se trata de utilizar la variable posteriormente esta generar un error 
del nombres

# Ejercicio: Realizar la iteracion de una lista de 0 a 10 de los numeros divisibles entre 3
for i in range(10):
    if i %3 == 0:
        print(i)
