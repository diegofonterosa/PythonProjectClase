#Ejercicio 1: Comparación de números y booleanos
#📌 Objetivo: Usar comparaciones con números y analizar los resultados booleanos.
#Crea tres variables numéricas con valores diferentes.
#Compara los valores entre sí (>, <, >=, <=, ==, !=).
#Almacena los resultados en nuevas variables booleanas y muéstralos.

numero1 = 34
numero2 = 685
numero3 = 2

mayor = numero1 > numero2
menor = numero3 < numero1
mayor_o_igual = numero2 >= numero3
menor_o_igual = numero3 <= numero2
igual = numero1 == numero2
distinto = numero2 != numero3

print(f"¿Es el numero1 mayor que el numero2? {mayor}")
print(f"¿Es el numero3 menor que el numero1? {menor}")
print(f"¿Es el numero2 mayor o igual que el numero3? {mayor_o_igual}")
print(f"¿Es el numero3 menor o igual que el numero2? {menor_o_igual}")
print(f"¿Es el numero1 igual que el numero2? {igual}")
print(f"¿Es el numero2 distinto que el numero3? {distinto}")

#Ejercicio 2: Propiedades y manipulación de cadenas
#📌 Objetivo: Trabajar con cadenas y métodos integrados de Python.
#Crea una cadena con una frase corta.
#Muestra cuántos caracteres tiene la cadena.
#Convierte toda la cadena a mayúsculas y minúsculas.
#Cuenta cuántas veces aparece una letra específica en la cadena.

frase_corta = "Me gustan los viernes"
cuantos_caractares = len(frase_corta)
print(f"La frase tiene {cuantos_caractares} caracteres")

mayusculas = frase_corta.upper()
minusculas = frase_corta.lower()
print(f"La frase en mayúsculas es {mayusculas}")
print(f"La frase en minúsculas es {minusculas}")

letra_a_contar = "e"
contar_letra = frase_corta.count(letra_a_contar)
print(f"La letra e aparece {contar_letra} veces")

#Ejercicio 3: Operaciones matemáticas con números y booleanos
#📌 Objetivo: Realizar cálculos numéricos usando valores booleanos.
#Define dos variables booleanas (verdadero, falso) con los valores True y False.
#Realiza operaciones matemáticas con estos valores (+, *, -).
#Muestra los resultados y analiza qué sucede.

verdadero = True
falso = False

suma = verdadero + falso
multiplicacion = verdadero * falso
resta = falso - verdadero

print(f"El resultado de la suma es {suma}, el resultado de la multiplicacion es {multiplicacion} y el resultado de la resta es {resta}")

#Ejercicio 4: Extracción de caracteres en una cadena
#📌 Objetivo: Extraer partes de una cadena utilizando índices y slicing.
#Define una cadena con una palabra o nombre.
#Extrae y muestra los tres primeros caracteres.
#Extrae y muestra los tres últimos caracteres.
#Extrae los caracteres en posiciones impares de la cadena.

cadena = "Alberto"

primeros_tres = cadena[:3]
ultimos_tres = cadena[-3:]
impares = cadena[::2]
print(f"Los tres perimeros caracteres son {primeros_tres}, los tres últimos son {ultimos_tres} y los caracteres impares son {impares}")

#Ejercicio 5: Conversión de tipos y evaluación booleana
#📌 Objetivo: Convertir entre tipos básicos y analizar valores booleanos.
#Convierte un número en una cadena y muestra el tipo de dato.
#Convierte una cadena numérica en un número entero y muestra el tipo.
#Convierte diferentes valores ("", "Texto", 0, 1, -1, None) a booleanos y muestra los resultados.

numero = 68
numero_a_cadena = str(numero)
print(f"El tipo de dato es {type(numero_a_cadena)}")

cadena_numero = "90"
numero_a_entero = int(cadena_numero)
print(f"El tipo de dato es {type(numero_a_entero)}")

print(bool(""))
print(bool("Texto"))
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(None))
