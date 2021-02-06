# Uso de metodos privados en python 3
# De la misma forma que para los atributos los metodos pueden volverse privados una ves que nosotros los declaramos con un doble guion bajo previo
# __NombreFuncion() estos solo pueden ser llamados desde un metodo publico dentro declarado dentro de la misma clase
# Tambien se puede declarar un atributo o una funcion como parcialmente privado si se lo declara solo con un guion bajo
# Estos pueden ser asignados o leidos al igual que los atributos publicos
class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre 
        self._apellido_paterno = ape_paterno
        self.__apellido_materno = ape_materno 
    
    # Metodo Publico        
    def metodo_publico(self):
        self.__metodo_privado()    
    
    # Metodo Privado
    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
    
    # Getters and Setters    
    def get_apellido_materno(self):
        return self.__apellido_materno
    
    def set_apellido_materno(self, ape_materno):
        self.__apellido_materno = ape_materno

# Declaracion de Objeto y llamada a metodo publico        
p1 = Persona("Juan", "Lopez", "Perez")
p1.metodo_publico()

# Impresion de atributos de una clase
print(p1.nombre)
print(p1._apellido_paterno)
print(p1.get_apellido_materno())
