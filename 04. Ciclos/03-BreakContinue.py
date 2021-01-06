# Uso de break y continue en ciclos de python
# El uso del comando break es para romper el ciclo y detener la ejecucion del mismo
# Impresion de la letra a solo la primera vez que se encuentra
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
else:
    print("Fin ciclo for")

# El uso del comando continue en un ciclo sirve para saltar una iteracion que no cumpla las condiciones dando paso a la siguiente
# Impresion de numeros pares dentro de un rango
# La funcion range permite la creacion de un array de numeros con la cantidad que se describe entre los parentesis range(n)
for numero in range(10):
    if numero % 2 == 0:
        print(numero)

for numero in range(10):
    if numero % 2 != 0:
        continue
    print(numero)
    