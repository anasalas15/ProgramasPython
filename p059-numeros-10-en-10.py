# Imprimir numeros de 1 a n de 10 en 10 

print('Imprimir numeros de 1 a n de 10 en 10')

n = int(input('Dame un numero ? '))

for i in range(1, n + 1, 10):
    print(i, end=' ')
    