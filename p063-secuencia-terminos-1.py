# Imprimir una secuencia de terminos armonicos armónicos el numero de renglones que el usuario desee y su suma

print('Imprime secuencia de numeros armonicos y su suma')

n = int(input('Cuantos terinos ? '))

suma = 0
secuencia = ""

for x in range(1, n + 1):
    termino = 1 / x  
    suma += termino
    secuencia += f'+ 1/{x}!' + " "

print(f'{secuencia} , suma: {suma}')
