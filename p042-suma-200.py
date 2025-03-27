# Calculo de suma de numeros >= 200 y mostrar cuantos numeros fueron 

print('Suma de numeros ')

while(True):
    sum  = 0 
    cont = 0

    while sum < 200:
        num = int(input('Introduzca un numero ? '))
        sum += num
        cont += 1

    print(f'\nSuma de numeros: {sum}')
    print(f'\nCantidad de numeros introducidos: {cont}')

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')
