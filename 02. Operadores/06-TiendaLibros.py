# Ejercicio 
# Creacion de una tienda de libros

# Registro de datos del libro
print("Proporcion los siguientes datos del libro")
print("-----------------------------------------")
nombre = input("Propociona el nombre del libro:")
id = int(input("Proporciona el ID del libro:"))
precio = float(input("Proporciona el precio del libro:"))
envio = input("Indica si el envio del libro es gratuito(S/N):")

if envio == "S" or envio == "s":
    envioGratuito = True
elif envio == "N" or envio == "n":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, el valor debe ser S/N"

# Impresion de los datos ingresados
print("-----------------------------------------")
print("Nombre:", nombre)
print("ID:", id)
print("Precio:", precio)
print("Envío Gratuito?:", envioGratuito)
