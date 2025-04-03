# Imprimir los pares de 2 a n y su suma 

print('Imprime los pares de 2 a n y su suma')

n = int(input('Dame un numero par: '))
s = 0

for i in range(2, n + 1, 2):
    print(i, end=' ')
    s += i

print(f'\nLa suma es = {s}')