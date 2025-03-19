# Suma numeros hasta 100

import os; os.system('clear')

c = 0 
s = 0

while c < 200:
    c += 1
    s += c 
    print(c, end=' ')
    if s >= 10000:
        print("\n")
        break
else:
    print('\n\nLlegamos a la meta')

print(f"Suma {s} , numero sumados para alcanzar la meta {c}")