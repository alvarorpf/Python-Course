# Usos extra en el manejo de clases
# La palabra self puede ser reemplazada por otra palabra, pero por uso comun de python se utiliza self
# Para realizar el envio de una tupla se utiliza la siguiente sintaxis *(nombre variable) *A por ejemplo
# Este tipo de parametros es opcional
# En caso de mandarse un diccionario se utiliza un diccionario
class Persona:
    def __init__(this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d

    def desplegar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Valores:", self.valores)
        print("Diccionario:", self.diccionario)
        
p1 = Persona("Alvaro", 27)
p1.desplegar()
# El envio de los valores de una tupla se los separa por coma una vez enviados los parametros iniciales
p2 = Persona("Andrea", 24, 3,6,7)
p2.desplegar()
# El envio de los valores de un diccionario se los envia mediante un conjunto de llave=valor despues de los valores previos enviados
p3 = Persona("Fabian", 4 , 4,9, m="Manzana", p="Pera", s="Sandia")
p3.desplegar()