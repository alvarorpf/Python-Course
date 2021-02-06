# Uso de encapsulamiento en python 3
# Para el uso del encapsulamiento a los atributos de una clase se declara los mismos con un doble guion bajo antes del nombre del mismo
# __NombreAtributo y para poder acceder o asignar valores a estos se deben utilizar las funciones set y get respectivamente
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    #Setters and Getters
    def get_nombre(self):
        return self.__nombre
            
    def set_nombre(self, nombre):
        self.__nombre = nombre   
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad         

# Declaracion de objeto y llamada a sus atributos        
p1 = Persona("Juan", 18)
print(p1.get_nombre())
print(p1.get_edad())

# Asignacion de otros valores al objeto previamente creado
p1.set_nombre("Karla")
p1.set_edad(20)
print(p1.get_nombre())      
print(p1.get_edad())