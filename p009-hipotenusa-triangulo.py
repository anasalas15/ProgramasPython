# Calculo de la hipotenusa de un triangulo rectangulo dadas las logitudes de sus lados

import math as m 
import os;os.system('clear')

print('Calculo de la hipotenusa de un triangulo rectangulo dadas las logitudes de sus lados')

longlado1 = float(input('Ingrese la longitud del primer lado :'))
longlado2 = float(input('Ingrese la longitud del segundo lado : '))

hipotenusa = m.sqrt(longlado1 * longlado1 + longlado2 * longlado2)

print(f'La hipotenusa es: {hipotenusa:.2f}')