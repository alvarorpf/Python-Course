# Ejercicios de la seccion de operadores con python

# Ejercicio 1
# Realice el calculo del area y el perimetro de un rectangulo

alto = int(input("Proporciona el alto:"))
ancho = int(input("Proporciona el ancho:"))

# Formula para el calculo del area de un rectangulo
area = alto * ancho

# Formula para el calculo del perimetro de un rectangulo
perimetro = (alto + ancho) * 2

# Mostrando los resultados
print("Area:", area)
print("Perimetro:", perimetro)

# Ejercicio 2
# Muestre el numero mayor de dos numeros ingresados por teclado

numero1 = int(input("Proporciona el Número 1:"))
numero2 = int(input("Proporciona el Número 2:"))

if(numero1 > numero2):
    print("Número 1 es mayor")
else:
    print("Número 2 es mayor")   