# Conversion de diferentes monedas a pesos mexicano
import os ; os.system('cls')

conv = {'USD':20.50,
        'EUR':22.30,
        'GBP':25.80,
        'JPY':0.19,
        'CAD':16.20
        }

print('Conversor de diferentes monedas a pesos mexicanos')
for m in conv.keys():
    print(m)

while True:
    mon = input('Moneda a convertir: ').upper()
    if mon in conv: break

cant = float ( input('Ingresa la cantidad a convertir: $'))

res = cant * conv[mon]

print(f'{cant} {mon} equivale a ${res:,.2f} MXN')