'''Realizar un programa que revise si una nota está aprobada (es decir si es mayor o igual a 4)
utilizando un if/else. La nota será ingresada por el usuario usando input().
'''

nota = float(input('ingrese la nota del alumno: \n'))

if nota >= 4:
    print(f'Aprobaste con: {nota}')
else:
    print(f'Desaprobaste con: {nota}')
