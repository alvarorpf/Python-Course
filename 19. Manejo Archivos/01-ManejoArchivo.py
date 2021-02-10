# Manejo de archivos en python 3 
# Para el manejo de archivos ya existen funciones predefinidas
# La funcion open nos permite abrir, crear o escribir archivos en la ruta que nosotros seleccionamos (r:Read, a:Append, w:Write, x: Create)
# Tambien podemos utilizar combinando los tipos de archivos (b:Binario, t: Texto) => (ab, wt, etc)
# Se pueden utilizar tambien de la siguiente forma (w+) para indicar que este archivo se leera y escribira
# La libreria os nos permite manejar las direcciones de las carpetas
# Con el metodo chdir nos dirigiremos a la carpeta del archivo en cuestion
# Con el metodo getcwd obtendremos la nueva ruta de la carpeta
import os

os.chdir('./19. Manejo Archivos/Recursos')
DIR = os.getcwd()

# Con las funcion open podemos realizar la creacion de un archivo en el directorio que nosotros especifiquemos
# Con la funcion write podemos realizar la escritura de informacion dentro de un archivo de tipo texto
try:
    archivo = open(DIR + "/prueba.txt", "w")    
    # Al final de cada linea se deberia registrar el salto de linea correspondiente
    archivo.write("Informacion de Archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:
    # Esta funcion nos permite cerrar el archivo en cuestion una vez cerrado el archivo ya no se puede escribir mas informacion dentro del mismo
    archivo.close()