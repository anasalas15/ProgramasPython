# Calculo del numero mayor 

print('Calculo del numero mayor')

while(True):
    mayor = None 

    while(True):
        num = int(input('Introduzca un numero ? '))

        if num == 0:
            break
        
        if mayor is None or num > mayor:
            mayor = num

    if mayor is not None:
         print(f'\nEl numero mayor es: {mayor}')
            

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')