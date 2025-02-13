# Dada una temperatura en grados celcius, se obtiene su equivalente en grados farenheit

import os;os.system('clear')

print('Dada una temperatura en grados celcius, se obtiene su equivalente en grados farenheit')

celcius = float(input('Dame la temperatura en grados celcius: '))
farenheit = (celcius * 9/5) + 32

print(f'La temperatura en grados farenheit es de: {farenheit:.2f}')


