# Diseño de clases en Python 3

class Producto:
    
    # Declaracion de variables estaticas
    contador_productos = 0
    
    # Inicializacion de la Clase
    def __init__(self, nombre, precio):
        # Debido a que la variable contador_producto es una variable de clase esta debe ser llamada desde la clase para realizar su incremento
        Producto.contador_productos += 1
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio
    
    # Impresion de la clase
    def __str__(self):
        return "ID Producto: " + str(self.__id_producto) + ", Nombre: " + self.__nombre + ", Precio: " + str(self.__precio)
    
    def get_precio(self):
        return self.__precio