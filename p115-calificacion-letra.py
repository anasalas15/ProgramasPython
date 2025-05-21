#Ejemplo de una funcion que regresa dos valores (dos cadenas)
import os

def calif_letra(p):
    l=''; m=''
    if p>=90 and p<100:  l='A'; m='Excelente'
    elif p>=80 and p<90: l='B'; m='Bien'
    elif p>=70 and p<80: l='C'; m='Suficiente'
    elif p>=60 and p<70: l='D'; m='Deficiente'
    elif p>=0 and p<60:  l='F'; m='Reprobado'
    return l, m

os.system('cls')
print('Dame tu promedio y te dare tu calificacion con letra y un mensaje ')
while True:
    p = int(input('Promedio (1-100): '))
    if p>=1 and p<=100: break

l, m = calif_letra(p)
print(f'Tu promedio es {p} corresponde a {l} y tu mensaje es {m}')
