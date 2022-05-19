'''Mini-desafío: Módulo
Un grupo de alumnos están cansados de estudiar.
Se les ocurre que puede ser una buena idea tomarse unos días para tomar sol y hacer ejercicio,
pero como no son para nada moderados, deciden organizar una ultramaratón de 4096 kilómetros.
La carrera empezará a medianoche, y se cronometra la cantidad de horas que tarda cada corredor
en finalizar.
Es probable que a los corredores les tome varios días lograr alcanzar la meta.

Realizar un programa al cual se ingresa la cantidad de
horas que tardó un corredor en alcanzar la meta,
y que muestra en pantalla la hora del día a la que llega.

Input ← 5

Output → 5 (Como tarda 5 horas, llega a las 5:00)

Input ← 20

Output → 20 (Como tarda 20 horas, llega a las 20hs)

Input ← 25

Output → 1 (Como tarda 25 horas, llega a la 1:00)

Input ← 45

Output → 21 (Como tarda 45 horas, llega a las 21:00)
'''

horasCorridas = int(input('ingrese la cantidad de horas que corrio el alumno: \n '))
## es un algoritmo sencillo donde se utilizara n%24 dando asi como resultado a la hora en la que llegara
## no asi los dias que tarda y la hora

horario = horasCorridas % 24

print(f'Como tarda {horasCorridas} horas, llegara  a las {horario} HS ')















