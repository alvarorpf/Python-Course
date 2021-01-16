# Uso de argumentos y parametros en funciones de python 3
# Un parametro es una variable definida entre los parentesis de una funcion
# Un argumento (arg) es el valor enviado a la funcion
# El uso de %s es para reemplazar el valor de una variable o parametro recibido o almacenado 
# si se usan mas de dos se debe encapsular entre parentesis
def funcion_arg(nombre, apellido):
    print("El nombre recibido es: %s %s" % (nombre, apellido))

funcion_arg("Alvaro", "Paredes")
