# imprimir la sucecion de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21...
'''
a = 0
b = 1
suma = 0
print(a, end = ' ')
print(b, end = ' ')
for i in range(0,10):
    suma = a+b
    a = b
    b = suma
    print(b, end = ' ')
'''
def fibonacci(n):
    a = 0
    b = 1
    suma = 0
    print(a, end = ' ')
    print(b, end = ' ')
    for i in range (0,n):
        suma = a+b
        a = b
        b = suma
        print(b, end = ' ')
