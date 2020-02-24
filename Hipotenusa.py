"""Hipotenusa de un triangulo"""

from math import sqrt

ladoA = float(input('Ingrese el valor de la longitud del lado A: '))
ladoB = float(input('Ingrese el valor de la longitud del lado B: '))

hipotenusa = sqrt(ladoA**2 + ladoB**2)

print('La longitud de la hipotenusa "lado C" del triangulo es:{}'.format(hipotenusa))


