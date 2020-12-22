# Ejercicio 1 
# Indicar la estacion del año desde el mes ingresado por teclado

mes = int(input("Proporciona el mes del año (1-12):"))

estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = "Verano"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Otoño"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Invierno"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Primavera"
else:
    estacion = "Valor incorrecto"

print("La estacion es: ", estacion, "para el mes", mes)