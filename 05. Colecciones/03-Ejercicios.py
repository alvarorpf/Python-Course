# Ejercicios con tuplas y listas en python
# Dada la siguiente tupla, 
# crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for: tupla = (13, 1, 8, 3, 2, 5, 8)
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
 
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
 
print(lista)