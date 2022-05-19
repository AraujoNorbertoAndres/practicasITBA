'''Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F de acuerdo a la siguiente conversión:

A: 90–100

B: 80–89

C: 70–79

D: 60–69

F: 0–59
'''

nota = float(input('Ingrese la nota: \n'))

if nota > 90 and nota <= 100:
    print('A')
elif nota > 80 and nota < 89:
    print('B')
elif nota > 70 and nota < 79:
    print('C')
elif nota > 60 and nota < 69:
    print('D')
elif nota >= 0 and nota < 59:
    print('F')
else:
    print('nota fuera de rango')
