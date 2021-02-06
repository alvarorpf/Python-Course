# Manejo de herencia multiple  en Python 3
# Clase 3
# En esta clase principal llamaremos a las otras clases que declaramos previamente.
# Primero se debe realizar la importacion de las mismas
from Color import Color
from Figura_Geometrica import FiguraGeometrica

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