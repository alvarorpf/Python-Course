# Lectura de archivos en python 3
# Cambio de directorio
import os
os.chdir('./19. Manejo Archivos/Recursos')
DIR = os.getcwd()

# Con la funcion read podemos leer el contenido del archivo
try:
    # Para evitar que se elimine un archivo cada vez que se llama se puede utilizar el comando a en lugar de r para que se anexe el nuevo contenido
    archivo = open(DIR + "/prueba.txt", "r")    
    # Lectura de archivos mediante la funcion read()
    # print(archivo.read())
    
    # Se puede indicar la lectura de cierta cantidad de caracteres del archivo que se este editando con el siguiente comando
    # Para poder ver su uso se debe comentar la linea print(archivo.read()) y descomentar la liena print(archivo.read(5))
    # print(archivo.read(5))
    
    # Se puede utilizar el comando readline() para leer linea por linea de un archivo
    # print(archivo.readline())
    
    # Iteracion de lectura de lineas
    # for linea in archivo:
    #    print(linea)
    
    # Lectura de todas las lineas en formato de lista mediante la funcion readlines
    # print(archivo.readlines())
    
    # Con este comando podemos obtener una linea en especifico en formato de lista
    # print(archivo.readlines()[1]) 
    
    # Nota: para poder utilizar cualquiera de las opciones se debe descomentar la linea que se desea revisar y comentar la lectura y escritura del archivo copia
    
    archivo2 = open(DIR + "/copia.txt", "w")
    archivo2.write(archivo.read() + "\n")
    archivo2.write("Nueva linea de archivo")
    
except Exception as e:
    print(e)
finally:
    # Esta funcion nos permite cerrar el archivo en cuestion una vez cerrado el archivo ya no se puede escribir mas informacion dentro del mismo
    archivo.close()
    archivo2.close()