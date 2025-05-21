#Convertir temperaturas de Farenheit a Celcius y viceversa usando funciones 
import os

def farenheit(t):
    r = (t * (9/5) ) + 32
    return r

def celcius(t):
    r = ( t -32 ) * ( 5/9 )
    return r

os.system('cls')
print('[F]arenheit ')
print('[C]elcius ')
op = input('Elige ? ').upper()

if op=='F':
    t = int(input('\nDame los grados Celcius ? '))
    r = farenheit(t)
    print(f'\n La temperatura en grados Farenheit es {r}')
elif op=='C':
    t = int(input('\nDame los grados Farenheit ? '))
    r = celcius(t)
    print(f'\n La temperatura en grados Celcius es {r}')
else:
    print('\Opcion invalida')

print('\nGracias por utilizar este programa')
