# Convercion de medidas de metros a km, m, cm y mm.
import os ; os.system('cls')

conv = {
    'km':1000,
    'm':1,
    'cm':0.01,
    'mm':0.001
}

long = int(input('Dame la longitud: '))

while True:
    unidad = input('Convertir: km, m, cm, mm ?').lower()
    if unidad in conv:
        break
res = long * conv[unidad]

print(f'{long} {unidad} son {res:,.2f} metros')