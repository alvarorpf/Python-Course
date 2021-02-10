# Uso de polimorfismo en python 3
# El polimorfismo es la ejecucion de una funcion ya sea que esta pertenezca a la clase padre o a la clase hija
# Esta dependera desde el contexto del cual se esta realizando el llamado al metodo
# Clase 3
from Empleado import Empleado
from Gerente import Gerente

# Creamos la funcion imprimir detalle el cual nos permitira llamar a la funcion __str__ desde el objeto o clase que se esta utilizando
def imprimir_detalles(objeto):
    print (objeto)
    print(type(objeto), end='\n\n')
    # El metodo is instance nos permite saber cual es la referencia o instancia que se esta utilizando en el tipo padre, este nos devuelve un valor booleano
    if isinstance(objeto, Gerente):
        print (objeto.departamento)

# Llamada desde la clase Empleado
e = Empleado("Alvaro", 3500.00)
imprimir_detalles(e)

# Llamada desde la clase Gerente
g = Gerente("Raquel", 2980.00, "Educacion")
imprimir_detalles(g)