# Uso de return en funciones de python 3
# La palabra return se utiliza para devolver una respuesta al ser llamada puede ser un valor o un manesaje

def suma(a,b):
    c = a + b
    return c

sum = suma(5,2)
print("La suma es: %s" % sum)

# Para evitar los errores en la recepcion de valores para los parametros podemos definir un valor para estos en la funcion
def resta(a=0, b=0):
    c = a - b
    return c
res = resta()
print("La resta es: %s " % res)

res = resta(a = 3)
print("La resta es: %s " % res)