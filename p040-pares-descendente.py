# Se imprimen numeros pares desde 100 hasta que el usuario decida (n)

print('Numeros pares descendientes')

while(True):
    n = int(input('Hasta que numero ? '))
    c = 100
    s = 0

    while c >= n :
        print(c, end=' ')
        s += c
        c -= 2

    print(f'\nSuma de numeros pares: {s}\n')

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')
