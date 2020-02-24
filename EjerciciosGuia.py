# -*- coding: utf-8 -*-
"""
Ejercicios guia python
"""
"-----------------------------------------------------------------------------------------------------------"
"EJERCICIOS SIMPLES"

"""Hipotenusa de un triangulo"""

from math import sqrt

ladoA = float(input('Ingrese el valor de la longitud del lado A: '))
ladoB = float(input('Ingrese el valor de la longitud del lado B: '))

hipotenusa = sqrt(ladoA**2 + ladoB**2)

print('La longitud de la hipotenusa "lado C" del triangulo es:{}'.format(hipotenusa))



"""Calculo de iva (19%) a un producto"""

precio = float(input('Ingrese el precio: '))

iva = precio * 0.19

precioIVA = precio + iva

print('El precio del producto incluyendo el IVA del 19% es:{}'.format(precioIVA))


"-----------------------------------------------------------------------------------------------------------"
"EJERCICIOS CON CONDICIONALES"

"""Número mayor o menor que 100"""

numero = float(input('Ingrese un numero: '))

if numero < 100:
    print ('El numero ingresado es menor que 100.\n')
elif numero == 100:
    print ('El numero ingresado es 100.\n')
elif numero > 100:
    print ('El numero ingresado es mayor que 100.\n')
    
    
    
"""Día de la semana según numero (del 1 al 7) ingresado"""

numero = float(input('Ingrese un numero del 1 al 7: '))

if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miercoles"
elif numero == 4:
    dia = "Jueves"
elif numero == 5:
    dia = "Viernes"
elif numero == 6:
    dia = "Sabado"
elif numero == 7:
    dia = "Domingo"
     
print('El dia de la semana correspondiente al numero ingresado(',numero,') es:{}'.format(dia))


"-----------------------------------------------------------------------------------------------------------"
"EJERCICIOS CON CILCOS"

"""Ciclo ¿desea continuar S/N?"""

respuesta = str(input("¿Desea continuar? escriba 'S' para responder si o 'N' para responder no: "))
while respuesta == "S":
    respuesta = str(input("¿Desea continuar? escriba 'S' para responder si o 'N' para responder no: "))
print("Adios")



"""Numeros del 1 al 100 en grupos de 10 por linea"""

print("Numeros del 1 al 100")
ctrol = 0
for i in range (1, 101):
    
    print (i, end=" ")
    ctrol = ctrol + 1
    
    if ctrol == 10:
        print ("")
        ctrol = 0


"-----------------------------------------------------------------------------------------------------------"
"EJERCICIOS CON COLECCIONES"

"""Media aritmetica de 5 numeros ingresados en una lista"""

print("Ingrese 5 numeros para hallar su media aritmetica")
listanumeros = []

for i in range(5):
    valor=int(input('Ingrese un numero: '))
    listanumeros.append(valor)

sumaelementos = 0
for i in range(5):
    sumaelementos = sumaelementos + listanumeros[i] 
    
promedio = sumaelementos / 5
print ("La media aritmetica de la lista de los 5 numeros es: ",promedio)



"""Veinte primeros numeros pares y su suma"""

print("Veinte primeros pares y su suma")
listapares = []
i, j = 0,2

while len(listapares) != 20:
    
    valor=j
    listapares.append(valor)
    ++i
    j=j+2

sumapares = 0
for i in range(20):
    sumapares = sumapares + listapares[i]     
    
print ("La suma de los 20 primeros pares es ",sumapares)


"-----------------------------------------------------------------------------------------------------------"
"EJERCICIOS CARACTERES"

"""Borrar blancos de una cadena de caracteres"""

mensaje = str(input("Escriba un mensaje cualquiera: "))

mensaje2 = mensaje.replace(' ', '')

print ("Mensaje sin blancos:",mensaje2,"")




"""Escribir cadena de caracteres al reves"""

cadena = input("Escriba un mensaje cualquiera: ")

for i in range(len(cadena),0, -1):    
    print (cadena[i-1], end="")


"-----------------------------------------------------------------------------------------------------------"
"FUNCIONES Y PROCEDIMIENTOS"

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


"-----------------------------------------------------------------------------------------------------------"
"RECURSIVIDAD"

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


"""Factorial recursivo"""

def factorialRec(n):
    if(n==0): 
        return 1;
    else:
        return n*factorialRec(n-1);
    
numerofact = int(input('Ingrese el numero a hallar el factorial: '))
fact = factorialRec(numerofact)

print("El factorial usando recursividad es ",fact)

"-----------------------------------------------------------------------------------------------------------"
"""MODULOS"""
 import modulos
 
num1 = int(input('Ingrese el primer numero: '))    
num2 = int(input('Ingrese el segundo numero: '))
 modulos.operaciones_modulo(num1,num2)

