# Operadores Logicos en Python
# Estos nos permiten comparar dos expresiones booleanas

# Declaracion de variables
a = int(input("Ingresa el valor de A:"))

# El operador (and) utiliza la siguiente comparacion
# True and True = True
# True and False = False
# False and True = False
# False and False = False
# Verificar si la variable A se encuentra dentro del rango
ValorMinimo = 1
ValorMaximo = 5
DentroRango = (a >= ValorMinimo) and (a <= ValorMaximo)
if DentroRango:
    print("A se encuentra en el siguiente rango[0,5]: ", DentroRango)
else:
    print("A no se encuentra en el rango [0,5]")

# El operador (or) utiliza la siguiente comparacion
# True or True = True
# True or False = True
# False or True = True
# False or False = False
# Verificar si la variable A se encuentra dentro del rango
Vacaciones = False
DiaDescanso = True
if (Vacaciones or DiaDescanso):
    print("Podemos realizar una actividad recreativa")
else:
    print("Tienes obligaciones que cumplir")
    
# El operador (not) utiliza la siguiente comparacion
# not True = False
# not False = True
# Invertir el valor de la comparacion anterior
Vacaciones = False
DiaDescanso = False
if (not(Vacaciones or DiaDescanso)):
    print("Tienes obligaciones que cumplir")
else:
    print("Podemos realizar una actividad recreativa")
    