# Calcular el numero de la suerte 

import os;os.system('clear')
print('Calcular el numero de la suerte')

año = int(input('Dame el año de nacimiento:  '))

u   = año % 10
año = año // 10
d   = año % 10
año = año // 10
c   = año % 10
año = año // 10
m   = año

suerte = u + d + c + m

print(f'Los digitos separados son:\n {m}\n {c}\n {d}\n {u} ')
print(f'Tu numero de la suerte es el {suerte}')

