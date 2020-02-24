"""Factorial recursivo"""

def factorialRec(n):
    if(n==0): 
        return 1;
    else:
        return n*factorialRec(n-1);
    
numerofact = int(input('Ingrese el numero a hallar el factorial: '))
fact = factorialRec(numerofact)

print("El factorial usando recursividad es ",fact)