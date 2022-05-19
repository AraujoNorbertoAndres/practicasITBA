'''
Mini-desafío: Funciones
Escribir una función que chequee los siguientes usuarios y contraseñas:

Usuario: Juan
Contraseña: 12345_

Usuario: Pablo
Contraseña: xDcFvGbHn

La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.
'''

def usuarioYContrasenia ( usuario,  contrasenia):
    if((usuario == 'Juan' or usuario == 'Pablo') and (contrasenia == '12345_' or contrasenia == 'xDcFvGbHn')):
        print('hola ', usuario , 'Ingresaste')
    else:
        print('Usuario o contraseña incorrectas')


