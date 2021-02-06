# Para utilizar las funciones contenidas en un archivo o modulo se debe realizar la importacion del mismo
# Se debe ingresar la carpeta que contiene al modulo y luego realizar la importancion del mismo
# Se puede renombrar el archivo para tener un mejor manejo de las funciones del modulo

from Modulos import Modulo as modulo

# Uso de las funciones contenidas en el archivo Modulo
resultado = modulo.sumar(5, 6)
print(resultado)

resultado = modulo.restar(5, 3)
print(resultado)