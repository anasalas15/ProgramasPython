# Introduce nombres de ciudades, cuenta cuantos son y cuales inician con consonante

import os; os.system('cls')

print("Introduce nombres de ciudades ")

ciudades = []

while True:
    nombre = input("Ingresa el nombre de una ciudad: ").strip()
    if nombre == "$":
        break
    ciudades.append(nombre)

print(f"\nCiudades: {ciudades}, se introdujeron {len(ciudades)} ciudades")

ciudades.sort(reverse=True)
print(f"\nLista ordenada en orden descendente: {ciudades}")

consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
ciudades_con_consonante = [c for c in ciudades if c.startswith(tuple(consonantes))]

print(f"\nCiudades que comienzan con consonante: {len(ciudades_con_consonante)}")
print("Nombres de ciudades con consonante inicial:")
for ciudad in ciudades_con_consonante:
    print(f"- {ciudad}")
