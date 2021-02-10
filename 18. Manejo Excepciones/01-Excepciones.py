# Manejo de excepciones en python 3
# Ya se encuentra un compilado de clases las cuales estan heredades para el manejo de excepciones en python 3
# En la carpeta recursos podemos observar las diferentes clases que se tienen para el manejo de excepciones
# Para manejar las excepciones en python se utilizan los comando try y except

# En caso de manejar todas las excepciones se debe ir aumentando las excepciones en orden de jerarquia de clase hija a clase padre
# Esto para obtener un mejor control de las excepciones

# La clase Exception es la clase padre de todas las demas excepciones
from IdenticosException import IdenticosException
# Excecion division por cero clase ZeroDivisionError
a = 10
b = 0
resultado = None
try:
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrio un error durante la ejecucion ZeroDivisionError: ", e)
    print(type(e))
print("El resultado es: ", resultado)
print("Continuamos con la ejecucion...")
print("================================")

# En este ejemplo podemos ver el proceso de los bloques de except de menor a mayor jerarquia
# Excepcion mezcla de datos clase TypeError
a = "10"
b = 0
resultado = None
try:
    resultado = a / b
except TypeError as e:
    print("Ocurrio un error durante la ejecucion TypeError: ", e)
    print(type(e))
except Exception as e:
    print("Ocurrio un error durante la ejecucion Exception: ", e)
    print(type(e))
print("El resultado es: ", resultado)
print("Continuamos con la ejecucion...")
print("================================")

# Excepcion error en conversion de variables ingresadas por teclado ValueError
# El bloque else permite ejecutar un bloque de codigo si no existio algun problema durante la ejecucion del try
# El bloque finally ejecuta un bloque de codigo ya sea que el try tenga o no una excepcion
res = None
try:
    a = int(input("Primer valor: "))
    b = int(input("Segundo Valor: "))
    res = a / b
except ValueError as e:
    print("Ocurrio un error durante la ejecucion ValueError: ", e)
    print(type(e))
except Exception as e:
    print("Ocurrio un error durante la ejecucion Exception: ", e)
    print(type(e))
else:
    print("No ocurrio ningun problema durante la ejecucion")
finally:
    print("Fin ejecucion de excepciones")
print("El resultado es: ", res)
print("Continuamos con la ejecucion...")
print("================================")


# Manejo de excepciones propias
# Para el uso de excepciones se pueden utilizar clases con exc propias asignando mensajes personalizados
try:
    a = 10
    b = 10
    if a == b:
        # Uso de Excepcion personalizada
        raise IdenticosException("Ocurrio un error de numeros identicos")
except Exception as e:
    print("Ocurrio un error durante la ejecucion Exception: ", e)
    print(type(e))


