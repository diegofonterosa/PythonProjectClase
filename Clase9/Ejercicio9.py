# Suma acumulativa

print("Introduce número para sumarlos y para acabar introduce 0")
numero = int(input())
resultado = 0

while numero != 0:
    resultado += numero
    numero = int(input())

print(f"El resultado es {resultado}")