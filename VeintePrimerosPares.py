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