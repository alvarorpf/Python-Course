# Manejo de clases en python 3

# Para la creacion de clases en python se recomienda que el nombre de la clase utilize como primera letra una mayuscula
# En caso de utilizar mas de una palabra, por cada una de las mismas se debera iniciar con una mayuscula

class Persona:
    
    # Metodo para inicializar la clase con sus parametros y valores
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # Declaracion de funciones dentro de la clase
    def imprimir(self):
        print("Bienvenido(a)", self.nombre, self.edad)
        
# Modificacion de Valores
Persona.nombre = "Alvaro"
Persona.edad = 27

# Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

# Creacion de un objeto
p = Persona("Andrea", 24)
print(p.nombre)
print(p.edad)
# Llamada a una funcion de la clase
p.imprimir()