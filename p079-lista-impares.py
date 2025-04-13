# Llena una lista con n numero impares, calcula la suma y promedio, muestra los divicibles entre 3 sumarlos y buscar un numero en la lista
import os; os.system('cls')

print("Llenar una lista con los primeros n números impares")

n = int(input("Cuantos numeros impares ?  "))

#Generar los primeros n numeros impares
impares = [2*i + 1 for i in range(n)]
print(f"\nLista de los primeros {n} números impares:\n{impares}")

#Sumarlos y calcular el promedio
suma = sum(impares)
promedio = suma / n

print(f"\nSuma total: {suma}")
print(f"Promedio: {promedio:.2f}")

#Numeros divicibles entre 3
div3 = [num for num in impares if num % 3 == 0]
suma_div3 = sum(div3)

print(f"\nNúmeros divisibles entre 3: {div3}")
print(f"Suma de números divisibles entre 3: {suma_div3}")

#Buscar un numero en la lista, imprimir la posicion 
buscar = int(input("\nNumero a buscar en la lista? "))
if buscar in impares:
    pos = impares.index(buscar)
    print(f"{buscar} esta en la lista, en la posicion {pos}")
else:
    print(f"{buscar} no se encuentra en la lista.")
