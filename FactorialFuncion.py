"""Funcion de factorial"""    

def factorial(n):
   if n==0 or n==1:
            res=1
   elif n != 0:
      res = n*factorial(n-1)
   return res

numfact = int(input('Ingrese el numero a hallar el factorial: '))
fact = factorial(numfact)

print("El factorial es ",fact)
