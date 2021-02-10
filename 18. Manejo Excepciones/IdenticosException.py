# Creacion de clase para excepciones propias
# Para crear excepciones propias las clases deben extender de la clase padre Exception
# Despues se debe inicializar el con la funcion __init__ para proporcionar un mensaje personalizado
class IdenticosException(Exception):
    def __init__(self, mensaje):
        self.menssage = mensaje