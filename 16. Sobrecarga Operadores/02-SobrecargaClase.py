# Uso de sobrecarga de operadores en Python 3
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    # Metodo sobreescrito de la clase padre object
    def __add__(self, otro):
        return self.__nombre + " " + otro.__nombre
    
    # Nota: Al sobreescribir un metodo declarado en una clase padre, este adquiere tambien la funcionalidad de la clase hija
    # Nota: Al realizar una sobrecarga de un metodo es adicionar una nueva funcionalidad a un metodo previamente declarado
p1 = Persona("Alvaro")
p2 = Persona("Raquel")
# Sobrecarga de signo + para la impresion de objetos
print(p1 + p2)

# Nota: en la carpeta adjunta se adicionan los archivos, con la lista de los operadores que se pueden sobrecargar
