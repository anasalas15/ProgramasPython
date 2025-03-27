# Se imprimen numeros impares desde 1 hasta que en usuario decida (n)

print('Numeros impares ascendentes')

while(True):
    n = int(input('Hasta que numero ? '))
    c = 1
    s = 0

    while c <= n :
        print(c, end=' ')
        s += c
        c += 2

    print(f'\nSuma de numeros impares: {s}\n')

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')
