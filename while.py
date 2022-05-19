'''
Implementar un programa que reciba 2 números (A y B),
y luego imprima en pantalla la secuencia de números enteros desde A hasta B.
En el caso de que B sea menor que A, se debe repetir el pedido de B hasta que sea válido ( B  ≥  A ).
'''

a = int(input('ingrese un numero: \n'))
b = int(input('\ningrese otro numero: \n'))

while a >= b:
    print('\ningrese los numeros nuevamente con el formato A < B ')
    print('\n')
    a = int(input('ingrese un numero: \n'))
    b = int(input('\n ingrese otro numero: \n'))
while a <=  b:
    print(a)
    a += 1

print('fin del programa')
