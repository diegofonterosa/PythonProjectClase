# Escribe un programa que pida al usuario una lista de números enteros separados por comas y
# calcule la suma de todos los elementos de la lista. El programa debe imprimir el resultado.

lista_numeros = input("Escribe una lista de numeros separados por coma: ").split(",")
resultado = 0

for i in range(len(lista_numeros)):
    resultado += int(lista_numeros[i])

print(f"Resultado: {resultado}")