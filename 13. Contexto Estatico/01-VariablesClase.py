# Manejo de variables estaticas en python 3

class MiClase:
    
    # La variable de clase se declara fuera de la funcion __init__
    # Esta variable se asocia con la clase como tal y no asi con los objetos que se vayan a crear con esta clase
    variable_clase = "Variable de Clase 1"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
# Las variables de clase pueden ser llamados sin la necesidad de crear un objeto previo de la clase como tal
print(MiClase.variable_clase)

# Se puede asignar un valor a las variables de instancia estas solo se asignan a la clase como tal y no al objeto creado antes o despues de la misma
MiClase.variable_instancia = "Variable Instancia 1"
print(MiClase.variable_instancia)

# Para llamar a una variable de instancia si o si se debe crear un objeto para almacenar su valor
o = MiClase("Variable de Instancia 2")
print(o.variable_instancia)

# A pesar de que las variables de clase no se encuentran listadas en los objetos creados, estas pueden ser accesedidas desde las mismas
print(o.variable_clase)

# Si se modifican los valores de las variables de clase desde un objeto, este solo se modifica para el objeto como tal y no asi para la clase
o.variable_clase = "Variable de Clase 2"
print(o.variable_clase)

# Si se crea otro objeto podemos ver que el valor de la variable de clase es el mismo que se encuentra declarada al inicio
o2 = MiClase("Variable Instancia 3")
print(o2.variable_clase)
print(o2.variable_instancia)

# Si se realiza una modificacion a la variable de clase todos los objetos creados tomaran este nuevo valor
# Menos los objetos que hayan modificado el valor de ese atributo
# Cambio en variable de clase
MiClase.variable_clase = "Variable Clase 3"

# Creacion de Objetos
o3 = MiClase("Variable de Instancia 4")
print(o3.variable_clase)
print(o3.variable_instancia)

o4 = MiClase("Variable de Instancia 5")
o4.variable_clase = "Variable de Clase 4"
print(o4.variable_clase)
print(o4.variable_instancia)