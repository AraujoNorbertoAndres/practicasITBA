'''
Mini-desafío: for

Realizar un programa para controlar el sistema de impresión de etiquetas con códigos de barras en un supermercado.
Primero se debe ingresar la cantidad de productos diferentes que necesitan etiquetas. Luego, para cada producto,
se ingresa el código a imprimir y la cantidad de veces que hay que imprimirlo. Posteriormente el programa imprimirá dicho código.
Imprimir en pantalla los códigos solicitados la cantidad requerida de veces.

>> 3 (cantidad total de productos)
>> 000000123 (primer código)
>> 1 (veces que hay que imprimir dicho código)
000000123
>> 123000789 (segundo código)
>> 3
123000789
123000789
123000789
>> 000031416 (tercer código)
>> 2
000031416
000031416
'''

productos = int(input('ingrese la cantidad de productos:\n'))

for producto in range(0, productos):
    cantidadEtiquetas = int(input('ingresar la cantidad de etiquetas para cada producto: \n'))
    codigo = input('\ncodigo de la etiqueta: \n')
    for etiqueta in range(0, cantidadEtiquetas):
        print(codigo)
    


















