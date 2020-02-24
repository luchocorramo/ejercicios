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

