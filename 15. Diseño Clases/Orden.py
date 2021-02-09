# Diseño de clases en Python 3

class Orden:
    
    # Declaracion de variables estaticas
    contador_ordenes = 0
    
    # Inicializacion de la clase
    # Se adiciono un valor por defecto a los productos, para que cuando al crear una nueva orden sin productos posteriormente se puedan agregar productos sin errores
    def __init__(self, productos=[]):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos
    
    # Impresion de la clase
    def __str__(self):
        productos_str = ""
        for p in self.__productos:
            productos_str += p.__str__() + ", "
        return "ID Orden: " + str(self.__id_orden) + ", Productos: [" + productos_str + "]"

    # Metodo para agregar productos
    def agregar_producto(self, producto):
        self.__productos.append(producto)
    
    # Metodos para sumar el total de deuda de la orden
    def calcular_total(self):
        total = 0
        for p in self.__productos:
            total += p.get_precio()
        return total
            
    