# Dados tres números enteros, verificar si son consecutivos

print('Dados tres números enteros, verificar si son consecutivos')
print('Dame tres numeros enteros separados por un espacio: ')

n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]

if n2 == n1 + 1 and n3 == n2 + 1:
    print('Son numeros consecutivos!')
else:
    print('No son consecutivos!')

