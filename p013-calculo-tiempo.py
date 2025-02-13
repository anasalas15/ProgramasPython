# Calculo de dias, minutos y segundos a partir de las horas 

import os;os.system('clear')

print('Calculo de dias, minutos y segundos a partir de las horas')

horas = int(input('Dame el numero de horas: '))

dias     = horas // 24
minutos  = horas * 60
segundos = minutos * 60

print(f'Dias: {dias}\nMinutos: {minutos}\nSegundos: {segundos}')


