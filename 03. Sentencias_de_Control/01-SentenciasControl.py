# Uso de sentencias de control en Python
# El uso de estas sentencias nos permite controlar el flujo de nuestro algoritmo dependeiendo las condiciones

condicion = True

if condicion:
    print("La condicion es verdadera") 
elif condicion == False:
    print("La condicion es falsa")
else:
    print("Condicion no reconocida")

# Ejercicio
numero = int(input("Ingrese un numero entre 1 y 3:"))
if numero == 1:
    numeroTexto = "Numero Uno"
elif numero == 2:
    numeroTexto = "Numero Dos"
elif numero == 3:
    numeroTexto = "Numero Tres"
else:
    numeroTexto = "El numero esta fuera del rango"
print("Numero proporcionado:", numeroTexto)