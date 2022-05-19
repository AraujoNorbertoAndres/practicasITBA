'''
Escribir una función que recibe un número N y retorna la cantidad de divisores del mismo.
Ejemplos:

contarDivisores(9) → 3 (El número 9 tiene 3 divisores: 1, 3, 9)

contarDivisores(10) → 4 (El número 10 tiene 4 divisores: 1, 2, 5, 10)
'''



def Divisores(x):
    
    for n in range(1, x):
        if(x%n)== 0:
            print(n)

    return x 







    
    
