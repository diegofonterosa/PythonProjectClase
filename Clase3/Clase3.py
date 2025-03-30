import math
import random
#1. len para mirar la longitude de una cadena o String
nombre = "Mario Flores"
print("Longitud del nombre: " , len(nombre))

#2. Upper y Lower para convertir los textos en mayúsculas o minúsculas
print("Quiero tener mi nombre en mayúsculas: " , nombre.upper())
print("Quiero tener mi nombre en minúsculas: " , nombre.lower())

#3. Slicing. Extraer partes de una cadena o String
# Dame los 3 primero cacteres
print("Los primeros 3 caracteres de mi nombre: " , nombre[:3])
# Dame los 4 últimos caracteres
print("Los 4 últimos caracteres de mi nombre: " , nombre[-4:])

#4. Reemplazar palabras en un String
frase = "Me encanta Java"
print("Quiero cambiar una palabra:" , frase.replace("Java" , "Python"))
#print("Impresión tras reemplazo de palabra:" , frase)

#5. Verificar si una cadena tiene o contiene a otra
print("Python" in frase) #False
nueva_frase = "Me encanta Python"
print("Python" in nueva_frase)#True

#6. Unir varias palabras en un solo String o cadena
palabras = ["Hola", "mundo", "Python"]
print("La frase completa es:", " ".join(palabras))

#7. Dividir una cadena en partes
oracion = "Python es divertido , el mejor"
palabras = oracion.split()
print("Lista de palabras:", palabras)

#8. Redondear un número que sea decimal
numero = 3.1416
print("El número PI redondeado es:", round(numero,3))

#9. Formatear números con decimales
precio = 19.99
print("Precios con dos decimales: {:.2f}".format(precio))

#10. Obtener el valor ASCII de un caracter
print("Código ASCII de 'A': ", ord('A'))

#11. Elevar un número al cuadrado
numerito = 5
print("5 elevado al cuadrado es: ", numerito **2)

#12. Obtener la raíz cuadrada
print("La raíz cuadra de 25 es: ", 25 ** 0.5)

#Alternativa importando sqrt con Math. Piensa que tienes el import arriba
numero_raiz = 16
raiz_numero = math.sqrt(numero_raiz)

print(raiz_numero)
print("Raíz cuadra del número es: ", raiz_numero)

#13. División, restos y módulos
print("División normal: ",10/3)
print("División entera: ",10//3)
print("Resto: ", 10%3)


#14. Generar números aleatorios
print("Dame un número aleatorio del 1 al 10: ", random.randint(1,10))

#15. Convertir cadenas a número y viceversa
numero_a_cadena = 100
texto = str(numero_a_cadena)
print("Convertido a texto, queda: ", texto)

cadena_a_numero ="200"
numero_a_cadena=int(cadena_a_numero)
print("Convertido a entero, queda: ", numero_a_cadena)

#16. Redondear siempre hacia arriba
print("Redondedo hacia arriba del número 3.2: ", math.ceil(3.2))
print("Redondedo hacia abajo del número 3.2: ", math.floor(3.2))

#17. Convertir una lista en un conjunto (eliminando duplicados)
numeros = [1,2,2,3,4,4,5]
sin_duplicados = set(numeros)
print("Lista sin duplicados: ", sin_duplicados)

#18. Absurdo PERO. Repetir una cadena varias veces
print("Python!"*3)

#19. Obtener el tipo de variable
dato = 9.98
print("Tipo de dato: ", type(dato))

#20. Combinar cadenas y variables en un print
nombreProfe = "Mario"
edad = 32
print(f"Hola soy {nombreProfe} y tengo {edad} años")