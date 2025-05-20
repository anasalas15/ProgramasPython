# Crear tres conjuntos de numeros, calcular operaciones y responder preguntas

import os; os.system('cls')

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print(f"Conjunto A: {A}\nConjunto B: {B}\nConjunto C: {C}")

print('\nUnion de conjuntos A y B')
print(f"A union B: {A | B}")

print('\nUnion de conjuntos B y C')
print(f"B union C: {B | C}")

print('\nDiferencia de A y C')
print(f"A diferencia C: {A - C}")

print('\nDiferencia simetrica de B y C')
print(f"B diferenia simetrica C: {B ^ C}")

print('\nInterseccion de B y C')
print(f"B interseccion C: {B & C}")

print('\nResponder las siguientes preguntas')
print(f"\nA es subconjunto de B ? : {A <= B} ")
print(f"C es subconjunto de A ? : {C <= A} ")
print(f"100 esta en A ? : {100 in A}")
print(f"60 esta en A, B y C ? : {60 in A and 60 in B and 60 in C}")
print(f"900 no esta en C ? : {900 not in C}")