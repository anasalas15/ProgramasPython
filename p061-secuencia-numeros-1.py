# Imprimir la secuencia de numeros mostrados el numero de renglones que el usuario desee

print('Imprimir una secuencia de numeros en piramide')
n = int(input('Dame un numero ? '))

for i in range(1, n+1):
    for j in range(i):
        print(i, end=' ')
    print()

    