'''
Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:
Si el número es par, se debe dividir por  2 .
Si el número es impar, se debe multiplicar por  3  y sumar  1 .
Este proceso se repite hasta llegar al numero  1  y luego muestra en pantalla la cantidad de pasos que tardó en llegar.
Ejemplos:

Input: 6
Output: 8 (Los pasos a seguir son: 6, 3, 10, 5, 16, 8, 4, 2, 1)
Input: 13
Output: 9 (Los pasos a seguir son: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1)
'''

def lothar(n):
    contador = 0
    while n > 1:
        if (n%2)==0:
            n = n/2
            print(int(n), end = ', ')
        else:
            n = (3*n)+1
            print(int(n), end = ', ')
        contador += 1

    return print(f'\n se necesitaron {contador} intentos')

        
    
    
