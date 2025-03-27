# Calcular la suma y promedio de una serie de numeros, hasta que el ususario introdusca 0

print('Calculo de suma y promedio ')

while(True):
    sum  = 0
    cont = 0

    while(True):
        num = int(input('Introduzca un numero ? '))
        if num == 0 :
            break
        sum += num 
        cont += 1
    
    if cont > 0 :
        prom = sum / cont
        print(f'\nSuma de numeros: {sum}')
        print(f'\nPromedio de numeros: {prom}')
        print(f'\nCantidad de numeros introducidos: {cont}')

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')


