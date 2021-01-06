# Uso de ciclo while en python
# Se debe tener cuidado con la condicion que se evalua en el ciclo while porque este puede ingresar en un bucle de ejecucion infinito

# Se puede utilizar el else en caso de que la condicion principal del ciclo no se cumpla
condicion = False
while condicion:
    print("Ejecutando Ciclo While")
else:
    print("Fin Ciclo While")
    
# Impresion de la variable i hasta llegar al valor 2
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Fin de Ejecucion")
    
# Ejercicio: Imprimir los valores de 0 a 10
i = 0
while i <= 10:
    print(i)
    i += 1