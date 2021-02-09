# Manejo de Clases Abstractas en python 3
# Como dato no se pueden crear objetos de clases que son declarados como abstractas
# Clase 1
# ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
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
    
    @abstractmethod
    def area(self):
        pass