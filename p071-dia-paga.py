# Dadas dos listas, los dias de la semana y la paga, encontrar la paga correspondiente al dia 

import os; os.system('cls')

print('Dadas dos listas, los dias de la semana y la paga, encontrar la paga correspondiente al dia ')

dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes','sabado','domingo']
paga = [700, 600, 500, 400, 300, 200, 100]
dia = ''
pos = total = 0

while True:
    dia = input('Dia de la semana (de lunes a domingo) ? ').lower()
    if dia in dias: break

print(f'Elegiste trabajar el: {dia}')

pos = dias.index(dia)
if pos == 5 or pos == 6 :
    total = paga[pos] * 4
else :
    total = paga[pos]

print(f'Paga = {total}')