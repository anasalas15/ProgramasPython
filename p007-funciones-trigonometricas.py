# Ejemplifica el uso de funciones trigonometricas del modulo math

import math as m 
import os;os.system('clear')

print('Calculo de las funciones trigonometricas basicas')
angulo = float( input('Dame un angulo en radianes ? ') ) 

seno     = m.sin(angulo)
coseno   = m.cos(angulo)
tangente = m.tan(angulo)
grados   = m.degrees(angulo)

salida = (
    'Resumen de funciones\n'
    f'El seno     : {seno}\n'
    f'El coseno   : {coseno}\n'
    f'La tangente : {tangente}\n'
    f'El angulo {angulo} en radianes, equivale a {grados} grados\n'
)

print(salida)

