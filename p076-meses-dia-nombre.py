# Imprimir dias del mes y nombre del mes 

import os; os.system('cls')
print('Imprimir dias del mes y nombre del mes ')

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
dias  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    n= int(input('Numero de mes ? '))
    if 1 <= n <= 12: 
       print(f'Elegiste el mes: {n}')
       print(f'El mes es: {meses[n - 1]}, los dias totales del mes son: {dias[n - 1]}')
    else:
        print('Error ')

    if(input('\nDeseas continuar? (S/N) ')).upper()=='N':break

print('\nHemos llegado al final..')