# Imprime un cuadro de asteriscos 

import os;
os.system('clear')

while(True):
    n = int(input('Cuantos renglones ? '))
    c = input('Caracter ? ')

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(c, end='')
        print()

    if input('\nDeseas continuar (S/N)? ').upper()=='N':
        break

print('\Hemos llegado al final ...') 