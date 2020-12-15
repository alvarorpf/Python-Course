# Operadores de Comparacion en Python
# Todos los operadores de comparacion daran como resultado un valor Booleano (True o False)

# Operador de Igualdad "=="
a = 3
b = 2
print("Variable A: ",a)
print("Variable B: ",b)
res1 = a == b
print("Igualdad: ", res1)

# Operador de Diferencia "!="
res2 = a != b
print("Diferencia: ", res2)

# Operador Mayor ">"
res3 = a > b
print("Mayor: ", res3)

# Operador Mayor Igual ">="
res4 = a >= b
print("Mayor Igual: ", res4)

# Operador Menor "<"
res5 = a < b
print("Menor: ", res5)

# Operador Menor Igual "<="
res6 = a <= b
print("Menor Igual: ", res6)

# Verificar si la variable a es divisible entre 2
if a % 2 == 0:
    print("A es un numero par")
else:
    print("A es un numero impar")
    
# Preguntar si una persona es mayor de edad
# La funcion int() permite convertir los valores ingresados por teclados a tipo numerico
EdadLimite = 18
EdadPersona = int(input("Ingrese su edad:"))
if (EdadPersona >= EdadLimite):
    print("Es una persona mayor de edad")
else:
    print("Es una persona menor de edad")
