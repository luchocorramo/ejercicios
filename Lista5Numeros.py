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