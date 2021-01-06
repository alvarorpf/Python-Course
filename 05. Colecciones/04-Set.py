# Colecciones de tipo set en python
# Las colecciones de tipo set no mantienen un orden en especifico y los elementos dentro del mismo son unicos
# No se pueden modificar elementos a una coleccion set pero si se pueden agregar o eliminar elementos del mismo
planetas = {"Marte", "Tierra", "Pluton"}
print(planetas)

# Tamaño de una coleccion de tipo set
print(len(planetas))

# Verificar si un elemento esta dentro de una coleccion set
print("Tierra" in planetas)

# Para agregar un nuevo elemento a la coleccion de tipo set se emplea el comando add despues de la variable
planetas.add("Jupiter")
print(planetas)

# No se pueden agregar elementos duplicados 
planetas.add("Tierra")
print(planetas)

# Eliminar elementos de una coleccion de tipo set mediante los metodos remove y discard
# La diferencia estre estos comandos es que el elemento discard no envia un error de eliminacion si no se encuentra un elemento en la coleccion
planetas.remove("Tierra")
print(planetas)

planetas.discard("Luna")
print(planetas)

# Limpiar todos los elementos de la coleccion
planetas.clear()
print(planetas)

# Eliminar toda la coleccion tipo set
del planetas
