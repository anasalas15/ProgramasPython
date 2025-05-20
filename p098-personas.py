# Crear dos conjuntos, calcular operaciones y mostrar diferentes afirmaciones

import os; os.system('cls')

A = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}

print(f'Conjunto A: {A}\nConjunto B: {B}')

print('\nUnion')
print(f"A union B: {A | B}")

print('\nInterseccion')
print(f"A interseccion B: {A & B}")

print('\nDiferencia')
print(f"A diferencia B: {A - B}")

print('\nDiferencia simetrica')
print(f"A diferenia simetrica B: {A ^ B}")

C = {'Pablo', 'Mateo'}
print('\nDemostrar si C es subconjunto de B')
print(f"C es subconjunto de B ? : {C <= B} ")

D = {'Reynaldo', 'Angelica'}
print('\nDemostrar si A es superconjunto de D')
print(f"A es superconjunto de D ? : {A >= D}")

print('\nVerificar la presencia de un elemento en los conjuntos')
print(f" Pedro esta en A ? : {'Pedro' in A}")
print(f" Lilia no esta en B ? : {'Lilia' not in B}")