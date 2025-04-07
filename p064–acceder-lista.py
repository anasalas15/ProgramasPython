## Ejemplificar el acceso a una lista de numeros

import os; os.system('cls')

nums = [10, 20, 30, 40, 50, 70, 10, 20, 99]

print('Acceder a los elementos de una lista c:')

print(f'La lista completa es: {nums}, y tiene {len(nums)} elementos')
print(f'El primer elemento es: {nums[0]}, y el ultimo elemento es: {nums[8]}')
print(f'El primer elemento es: {nums[-9]}, y el ultimo elemento es: {nums[-1]}')
print(f'Los elementos del 2 al 6: {nums[2:6]}')
print(f'Los primeros tres elementos: {nums[6:]}')