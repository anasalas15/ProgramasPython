# El ususario adivina un numero entero al azar entre 1 y 100

import random;

while(True):
    ns = random.randint(1,100)
    i = 0

    while(True):
        n = int(input('Adivina cual es el numero secreto ? '))
        i += 1 
        if n == ns:
            print(f'Felicidades !Adivinaste e numero en {i} intentos')
            break
        elif n < ns:
            print('El numero es mas grande')
        else:
            print('El numero sectreto es mas pequeño')
    
    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')

