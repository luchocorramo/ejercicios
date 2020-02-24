"""Funcion potencia"""

def potencia (n,p):
    
    numpotencia = 1
    for i in range (p):
        numpotencia = numpotencia*n
    return numpotencia
     
numpotencia = int(input('Ingrese el numero que desea sacarle potencia: '))    
pot = int(input('Ingrese la potencia que le desea calcular: '))

result = potencia(numpotencia,pot)
print("El resultado es ",result)
