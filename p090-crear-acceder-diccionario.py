# Diccionario de dias de las semanas

import os; os.system('cls')

dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miercoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sabado',
    7: 'Domingo'
}

print(f'Los dias de la semana {dias} - {len(dias)}')

#Obtener elementos usando []
print(f'\nPrimer elemento: {dias[1]}')
print(f'\nUltimo elemnto: {dias[7]}')

#Obtener elementos usando get()
print(f'\nEl quinto elemento es: {dias.get(5)}')
print(f'\nEl Septimo elemento es: {dias.get(7)}')

print('\nDiccionario completo en tabla\n')
for k, v in dias.items():
    print(f'   {k:<7} : {v}')