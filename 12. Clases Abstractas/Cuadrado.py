# Manejo de Clases Abstractas  en Python 3
# Clase 3
# En esta clase principal llamaremos a las otras clases que declaramos previamente.
# Primero se debe realizar la importacion de las mismas
from Color import Color
from FiguraGeometrica import FiguraGeometrica

# No se puede realizar la creacion directa de clases abstractas debido a que estos no pueden ser creados
# fig = FiguraGeometrica()
# Si las clases que son heredadas no cuentan con la funcion que es declarada como abstracta las clases que se van heredando se vuelven abstractas

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def __str__(self):
        a = self.area()
        return FiguraGeometrica.__str__(self) + ", "+ Color.__str__(self) + ", Area: " + str(a)
        
    def area(self):
        return self.get_alto() * self.get_ancho()

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
    
    def __str__(self):
        a = self.area()
        return FiguraGeometrica.__str__(self) + ", "+ Color.__str__(self) + ", Area: " + str(a)
    
    # Si se comenta este par de lineas podemos observar que si no se declara esta funcion area la clase Rectangulo pasa a ser abstracta
    # Por lo tanto no se podran crear objetos de esta clase        
    def area(self):
        return self.get_alto() * self.get_ancho()

# Creacion del Objeto Cuadrado
c1 = Cuadrado(4, "Amarillo")
print(c1)
# Funcion para ver el orden en el cual se estan llamando las clases para ser ejecutadas
print(Cuadrado.mro())

# Creacion del Objeto Rectangulo
r1 = Rectangulo(2,4,"Morado")
print(r1)
print(Rectangulo.mro())