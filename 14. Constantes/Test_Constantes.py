# Uso de Constante en Python 3
# Para llamar a una constante desde otro archivo es necesario importar la misma

# Se puede importar de forma separada las declaraciones de los modulos para ser renombradas

from Constantes import MI_CONSTANTE as MC
from Constantes import Matematicas as Mat

# Se puede utilizar esta linea de codigo para importar todas las declaraciones del archivo creado

from Constantes import *

print(MI_CONSTANTE)
print(MC)
# Una constante se vuelve en una variable de clase
print(Matematicas.PI)
print(Mat.PI)

# Llamando a los valores importados estos pueden ser modificados, las siguientes llamadas adquiriran este nuevo valor asignado
MI_CONSTANTE = "Nueva Declaracion"
Mat.PI = 3.1416
print(MI_CONSTANTE)
print(Mat.PI)