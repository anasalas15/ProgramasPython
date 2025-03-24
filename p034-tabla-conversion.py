# Tabla de conversion de pesos a dolares, en un rango de valores

import os;

while(True):
    os.system('clear')
    tc = 20.5 ; tl = 25.97
    print('Tabla de conversion de peso a dolar \n')
    pi = float(input('Valor inicial : '))
    pf = float(input('Valor final   : '))
    c = pi
    print('\nPeso\tDollar\tLibra')
    print('-'*25)
    while c <= pf:
        print(f'{c}\t{c/tc:.2f}\t{c/tl:.2f}')
        c += 1
    print('-'*25)

    if input('Deseas Continuar (S/N) ? ').upper()=='N': break

print('\nProceso terminado \n')

