# Ingrese un valor por teclado y muestre la nota obtenida
calificacion = int(input("Proporciona una calificación entre 0 y 10: "))
#Si esta entre 9 y 10 imprimir: A
if calificacion >= 9 and calificacion <= 10:
    print("A")
#Si esta entre  8 y menor a 9 imprimir: B
elif calificacion >= 8 and calificacion < 9:
    print("B")
#Si esta entre 7 y menor a 8 imprimir: C
elif calificacion >= 7 and calificacion < 8:
    print("C")
#Si esta entre 6 y menor a 7 imprimir: D
elif calificacion >= 6 and calificacion < 7:
    print("D")
#Si esta entre 0 y menor a 6 imprimir: F
elif calificacion >= 0 and calificacion < 6:
    print("F")
#Si no esta en el rago, imprimir: Valor desconocido
else:
    print("Valor desconocido")