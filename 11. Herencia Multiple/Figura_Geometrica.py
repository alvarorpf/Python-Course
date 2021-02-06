# Manejo de Herencia multiple en python 3
# Clase 1
class FiguraGeometrica():
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho
        
        # Getters and Setters    
    def get_alto(self):
        return self.__alto
    
    def get_ancho(self):
        return self.__ancho
    
    def set_alto(self, alto):
        self.__alto = alto
    
    def set_ancho(self, alto):
        self.__ancho = ancho
    
    def __str__(self):
        return "Alto: " + str(self.__alto) + ", Ancho: " + str(self.__ancho)