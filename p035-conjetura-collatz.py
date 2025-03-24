# Calcular la conjetura de collatz


while(True):
    print('Imprime la Conjetura de Collatz \n')
    n = int(input('Dame un numero de pasos positivo  ? '))
    c = 0 
    while n != 1 :
        print(n, end=' ')
        c += 1
        if n % 2 == 0:
            n = n // 2 
        else:
            n = n * 3 + 1 
    print(n, end=' ')
    print('\nPasos: ', c)

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')