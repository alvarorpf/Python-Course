# Manejo de herencia entre clases en Python 3

# Declaracion de Clase Persona
# Atributos: nombre, edad
# La funcion str sirve para la impresion de los valores en lugar de la direccion de memoria
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return "Nombre: "+ self.nombre + ", Edad: " + str(self.edad)

# Declaracion de Clase Empleado
# Atributos: Sueldo
# Se pone la clase padre entre parentesis para saber de que clase se esta realizando la herencia
# Con la funcion super() se llamaran a los atributos o funciones de la clase padre
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        # return super().__str__() + ", Sueldo: " + str(self.sueldo)
        return "Empleado: "+ self.nombre + ", Edad: " + str(self.edad) + ", Sueldo: " + str(self.sueldo)

# Creacion de objetos
persona = Persona("Alvaro", 28)
print(persona)
empleado = Empleado("Andrea", 25, 1200)
print(empleado)
empleado.nombre = "Raquel"
empleado.sueld  o = 1250.90
print(empleado)