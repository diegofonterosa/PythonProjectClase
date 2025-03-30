#Ejercicio 1. Crea un diccionario simple
persona = {
    "nombre" : "Diego",
    "edad" : 43,
    "registradoEnElCenso" : True
}
print(persona)

#Ejercicio 2.
#Subapartado del 1

print(persona["edad"])

#Ejercicio 3.
#Añadir una nueva clave-valor

persona["ciudad"] = "Burgos"
print(persona)

#Ejercicio 4.
persona["edad"] = 44
print(persona)

#Ejercicio 5
#Elimina una clave
del persona["ciudad"]
print(persona)

#Ejercicio 6.
#Comprobar si una clave existe
existe_nombre = "nombre" in persona
print(existe_nombre)

#ejercio 7.
#Compara dos valores booleanos

es_mayor_y_registrado = persona["edad"]>18 and persona["registradoEnElCenso"]
print(es_mayor_y_registrado)


#Ejercicio 8.
#Uso del not con un boolean

no_registrado = not persona["registradoEnElCenso"]
print(no_registrado)

#Ejercicio 9
#Elimina duplicados

numeros = [1,2,2,3,4,5,3,4,5,2,1]
conjunto = set(numeros)
print(conjunto)

#ejercicio 10
#compara si dos colecciones tienen los mismos elementos unicos

lista_a=set([1,2,3,4])
lista_b=set([4,3,2,1])
mismos_elementos = lista_a==lista_b
print(mismos_elementos)

#Ejercicio 1: Evaluación de Expresiones Booleanas
#📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
#Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
#Muestra el valor booleano de cada una.

#expresion1 = 10>5
#expresion2 = 7+3 == 10
#expresion3 = 20<15
#expresion4 = 4*2==9
#print(expresion1, expresion2, expresion3, expresion4)



#Ejercicio 2: Operaciones Matemáticas con Booleanos
#📌 Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
#Suma True + True y False + True.
#Multiplica True * 10 y False * 50.
#Muestra los resultados y explica qué ocurre.

#print(True+True)
#print(False+True)
#print(False+False)
#print(True*10)
#print(False*50)


#Ejercicio 3: Conversión entre Tipos Básicos
#📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
#Convierte un número en cadena y muéstralo.
#Convierte una cadena numérica en un entero.
#Convierte un booleano en un número.

#print(int(True))
#print(int(False))



#Ejercicio 4: Propiedades de las Cadenas
#📌 Objetivo: Manipular cadenas y explorar sus propiedades.
#Crea una cadena con tu nombre.
#Muestra el primer y último carácter.
#Muestra la longitud de la cadena.
#Convierte la cadena a mayúsculas y minúsculas.

#nombre = "Diego"
#print(nombre[0])
#print(nombre[-1])
#print(nombre[4])
#print(nombre[-2])
#print(nombre[-3])
#print(nombre[-4])
#print(nombre[-5])

#Ejercicio 5: Operaciones con Cadenas y Números
#📌 Objetivo: Realizar operaciones matemáticas con cadenas y números.
#Concatenar cadenas con números usando str().
#Multiplicar una cadena para repetirla varias veces.

# concatenar un número con una cadena usando str()
edad = 25
mensaje = "Tengo " + str(edad) + " años."
print(mensaje)  # "Tengo 25 años."
# repetir una cadena varias veces
repetido = "Hola " * 3
print(repetido)  # "Hola Hola Hola "


#Ejercicio 6: Operaciones con Caracteres y Códigos ASCII
#📌 Objetivo: Explorar caracteres y su representación en ASCII.
#Obtén el código ASCII de la letra 'A'.
#Convierte un número en su carácter ASCII correspondiente.

# obtengo el código ASCII de una letra
codigo = ord('A')
print(codigo)  # 65
# convierto un número en un carácter
letra = chr(66)
print(letra)  # "B"


#Ejercicio 7: Evaluación de Expresiones Lógicas
#📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
#Evalúa expresiones lógicas combinando números y operadores lógicos.
#Muestra los resultados.

# evalúo expresiones con operadores lógicos
print(10 > 5 and 3 < 8)  # True porque ambas condiciones son verdaderas
print(5 == 5 or 2 > 10)  # True porque al menos una condición es verdadera
print(not (4 == 4 and 3 > 1))  # False porque el 'not' invierte el resultado
