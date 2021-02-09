# Diseño de clases en Python 3
# Importacion de clases
from Orden import Orden
from TestProducto import *

# Creacion de lista de productos para asignar a la orden
# La funcion .append() es utilizada para adicionar un elemento a un array

# Creacion de objetos de tipo orden
# Primera orden: Creacion de una lista vacia y agregado de productos con funcion append()
lista_productos = []
lista_productos.append(p1)
lista_productos.append(p3)
lista_productos.append(p5)
o1 = Orden(lista_productos)
print(o1)
print("El precio total es: ", o1.calcular_total())

# Segunda orden: Creacion de un array con productos 
lista_productos = [p2, p4, p6]
o2 = Orden(lista_productos)
print(o2)
print("El precio total es: ", o2.calcular_total())

# Tercera Orden: Creacion de una orden sin productos y uso de funcion agregar_producto
o3 = Orden()
o3.agregar_producto(p1)
o3.agregar_producto(p2)
o3.agregar_producto(p3)
o3.agregar_producto(p4)
print(o3)
print("El precio total es: ", o3.calcular_total())