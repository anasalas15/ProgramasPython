# Dado un numero entero como base y un numero entero como exponente, calcular la base elevado al exponente

import os; os.system('clear')

base = int(input('Base  ? '))
exp = int(input('Exponente ? '))

r = 1

for _ in range(exp):
    r = r * base

print(f'{base} ^ {exp} = {r}')

