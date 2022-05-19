'''
Mini-desafío: Operadores
1.Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, y se
   muestre a la salida el promedio de los tres números.

2.Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, y se
   muestre a la salida la media geométrica de los tres números.
'''

##para sacar la medida geometrica es la n-sima raiz cuadrada del producto de n numeros
##Formula
## (x1 * x2 * x3 ... xn)**(1/n)

## en este caso solo se ingresaran tres numeros(por conveniencia) cualesquiera

a = int(input('ingrese el primer numero: '))
b = int(input('ingrese el segundo numero: '))
c = int(input('ingrese el tercer numero: '))

medidaGeometrica = (a * b * c)**(1/3)

input(f'La medida geometrica entre {a}, {b}, {c} es: {medidaGeometrica}' )



