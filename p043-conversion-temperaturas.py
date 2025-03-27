# Calculo de temperatura convertida de centigrados a farenheit de un rango de valores introducidos

print('Temperatura de centigrados a farenheit de un rango de valores')

while(True):
    tempi = float(input('Ingresa la temperatura inicial en grados centigrados ? '))
    tempf = float(input('Ingresa la temperatura final en grados centigrados ? '))

    centigrados = tempi

    while centigrados <= tempf:
         farenheit = ( centigrados * 9/5 ) + 32
         print(f'{centigrados:.2f} Grados Centigrados = {farenheit:.2f} Grados Farenheit')
         centigrados += 1

    if input('Deseas Continuar (S/N) ? ').upper() == 'N': break

print('\nProceso Terminado ')

    
