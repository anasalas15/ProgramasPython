# Suma de n numeros introducidos por el usuario usando ciclo for

import os;

while(True):
    os.system('clear')

    cuantos = int(input('Cuantas calificaciones deseas procesar ? '))
    suma = 0
    cadnum = ""

    for i in range(1, cuantos+1):
        n = int(input(f'Calificacion[{i}] = '))
        suma += n 
        cadnum = cadnum + ' ' + str(n) 

    print(f'Los numeros que introdugiste fueron: {cadnum}')
    print(f'La suma es {suma}, el promedio es {suma / n}')

    if input('\nDeseas continuar (S/N)? ').upper()=='N':break

print('\Hemos llegado al final ...') 