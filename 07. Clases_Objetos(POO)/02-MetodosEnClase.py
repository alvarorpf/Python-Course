# Uso de metodos en las clases en python 3
class Aritmetica:
    """Clase aritmetica para realizar las operaciones matematicas basicas"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        """Se realiza la operacion de suma con los atributos de la clase"""
        return self.operando1 + self.operando2
        
    def restar(self):
        """Se realiza la operacion de resta con los atributos de la clase"""
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        """Se realiza la operacion de resta con los atributos de la clase"""
        return self.operando1 * self.operando2
    
    def dividir(self):
        """Se realiza la operacion de resta con los atributos de la clase"""
        return self.operando1 / self.operando2

suma = Aritmetica(10,5)
print("La suma del objeto es:", suma.sumar())

resta = Aritmetica(20,16)
print("La resta del objeto es:", resta.restar())

multiplicar = Aritmetica(5,5)
print("La suma del objeto es:", multiplicar.multiplicar())

dividir = Aritmetica(14, 7)
print("La resta del objeto es:", dividir.dividir())

# Laboratorio 1
# Escribir un programa que permita leer los atributos de base y altura para calcular el area del rectangulo
class Rectangulo:
    """Clase Rectangulo"""            
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    """Funcion para realizar el calculo del area de un rectangulo"""
    def calcular_area(self):
        return self.base * self.altura

base = int(input("Ingrese un valor numerico para la base del rectangulo:"))
altura = int(input("Ingrese un valor numerico para la altura del rectangulo:"))
rec = Rectangulo(base, altura)
print("El Area del rectangulo es: ", rec.calcular_area())

# Laboratorio 2
# Escribir un programa para calcular el volumen de una caja
class Caja:
    """Inicio de la clase Caja"""
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
    
    """Funcion para calcular el volumen de una caja"""
    def calcular_volumen(self):
        return self.alto * self.ancho * self.largo

alto = int(input("Ingrese el alto de la caja:"))
ancho = int(input("Ingrese el ancho de la caja:"))
largo = int(input("Ingrese el largo de la caja:"))
caja = Caja(alto, ancho,largo)
print("El volumen de la caja es: %s m3" % caja.calcular_volumen())