# Ejemplificar como se itera sobre una lista de numeros

import os; os.system('cls')

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print('\n\nDiferentes formas de iterar (pasar por todos los elementos) de una lista')

print(f'La lista original es {nums}, longitud {len(nums)} elementos')

print('\n\n1. Iterar sobre la lista, usando un ciclo for sin subindice')
for n in nums:
    print(n, end='')

print('\n\n2. Iterar sobre la lista, usando un ciclo for con subindice')
for _ in range(len(nums)):
    print(nums[_], end='')

print('\n\n 1b. Iterar sobre la lista, imprimir cada valor sumandole 2')
for n in nums:
    print(n + 2, end='')
print(f'La lista original es {nums}, longitud {len(nums)} elementos')

print('\n\n 2b. Iterar sobre la lista, usando un ciclo for con subindice')
for _ in range(len(nums)):
    print(nums[_], end='')
    nums[_] = nums[_] ** 2
print(f'\nLos numeros son {nums}, longitud {len(nums)} elementos') 