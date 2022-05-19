'''
Una buena e-stimación
El número  e  tiene inmensa utilidad para el análisis y la estadística, es una
de las super-estrellas de la matemática, y su utilidad radica en que la función
ex  es igual a su derivada, por definición de  e .

Gracias a las series de Taylor podemos obtener la siguiente definición del número  e :

e=1+1/1!+1/2!+1/3!+1/4!+1/5!+... 

Se pide obtener una aproximación del número  e  calculando la suma de los primeros  20  términos de esta serie.

Tips:
n!=1⋅2⋅3⋅ ... ⋅n .
'''

def factorial(n):
  a=1
  for i in range (1,n+1):
    a *= i
  return a

def euler(m):
  e = 1
  for i in range(1,m):
    e += 1/factorial(i)
  return e
