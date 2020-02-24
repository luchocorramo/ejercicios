"""Escribir cadena de caracteres al reves"""

cadena = input("Escriba un mensaje cualquiera: ")

for i in range(len(cadena),0, -1):    
    print (cadena[i-1], end="")