"""Numeros del 1 al 100 en grupos de 10 por linea"""

print("Numeros del 1 al 100")
ctrol = 0
for i in range (1, 101):
    
    print (i, end=" ")
    ctrol = ctrol + 1
    
    if ctrol == 10:
        print ("")
        ctrol = 0

