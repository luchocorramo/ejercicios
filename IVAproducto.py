"""Calculo de iva (19%) a un producto"""

precio = float(input('Ingrese el precio: '))

iva = precio * 0.19

precioIVA = precio + iva

print('El precio del producto incluyendo el IVA del 19% es:{}'.format(precioIVA))
