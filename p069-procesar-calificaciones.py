# Procesar n calificaciones introducidas por un usuario

import os; os.system('cls')

print('Procesamiento de calificaciones ...')

nums = []
mp = []
n = suma = prom = 0

while n != 999:
    n = float(input("Calificaciones[1-10] > "))
    if n>0 and n<=10:
        nums.append(n)
    else:
        print(':(')

print(f"\n Fin > {nums} - {len(nums)} ")

suma = sum(nums)
prom = suma / len(nums)

for n in nums :
    if n > prom:
        mp.append(n)

print('\n\nEstadisticas')
print(f'La suma es          = {suma}')
print(f'El promedio es      = {prom}')
print(f'Mayores al promedio = {mp} - {len(mp)}')