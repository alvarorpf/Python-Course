# Manejo de Clases Abstractas en python 3 
# Clase 2
class Color:
    def __init__(self, color):
        self.__color = color
    
    #Set and Get
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
        
    def __str__(self):
        return "Color: " + self.__color