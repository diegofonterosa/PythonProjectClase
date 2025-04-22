#Ejercicio 4 - Múltiplos de 3 y 5

numero = int(input("Introduce un número entero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} es múltiplo de 3 y de 5")
elif numero % 3 == 0:
    print(f"{numero} es múltiplo de 3")
elif numero % 5 == 0:
    print(f"{numero} es múltiplo de 5")
else:
    print(f"{numero} no es múltiplo ni de 3 ni de 5")

