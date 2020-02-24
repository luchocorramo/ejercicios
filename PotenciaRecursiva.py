"""Potencia recursiva"""

def potenciaRec (n,p):
    
    if p == 0:
        return 1;
    else:
        return n*potenciaRec(n,p-1)
     
numeropot = int(input('Ingrese el numero que desea sacarle potencia: '))    
expo = int(input('Ingrese la potencia que le desea calcular: '))

result = potenciaRec(numeropot,expo)
print("El resultado es ",result)