import math
import random

#1. Generador de nombres de usuario

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
nombre_usuario = (nombre + apellido).lower().replace(" ", "")
print("Tu nombre de usuario es:", nombre_usuario, random.randint(100, 999))

#2. Analizador de frases

frase = input("Introduce una frase: ")
cantidad_caracteres = len(frase)
print("La frase tiene", cantidad_caracteres,"caracteres")
print("Python" in frase)
print("La fase en mayúsculas es: ", frase.upper())

#3. Cálculo de descuentos
precio = float(input("Introduce un precio: "))
descuento = precio * 0.15
precio_final = precio - descuento
print("El precio con descuento es: ", precio_final)
print("El precio redondeado es ", math.ceil(precio_final))

#4. Generador de etiquetas de productos
nombre_producto = input("Introduce el nombre del producto: ")
precio_producto = float(input("Introduce el precio del producto: "))

nombre_producto = nombre_producto.upper()
precio_formateado = "{:.2f}".format(precio_producto)
codigo_ASCII = ord(nombre_producto[0])

print("ETIQUETA DEL PRODUCTO")
print("+++++++++++++++++++++++++++")
print("Nombre Producto: ", nombre_producto)
print("Precio Producto: ", precio_formateado)
print("Codigo ASCII: ", codigo_ASCII)
print("+++++++++++++++++++++++++++")

#5. Conversión de tipos y manipulación de lista
numeros_usuario = input("Introduce una lista de números separados por una coma: ")

lista_numeros = list(set(map(int, numeros_usuario.split(","))))
print("La lista de números ordenada y sin duplicados es: ", lista_numeros)

#6. Creación de mensajes personalizados
nombre_usu = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
ciudad = input("Escribe la ciudad donde vives: ")

edad_redondeada = math.ceil(edad/18)*18
print(f"Tu nombre es {nombre_usu}, tienes {edad} años y vives en {ciudad}. Edad mínima adulta {edad_redondeada}")

#7. Generador de contraseñas aleatorias
usuario_nombre = input("Introduce tu nombre: ")

contraseña=f"{usuario_nombre[0].upper()}{random.randint(100,900)}+"

print(f"Tu nueva contraseña es: {contraseña}")

#8. Verificación de nombres en listas

usu_nombre = input("Introduce tu nombre: ")

lista_invitados = ["Diego","Marcos","Pablo"]

if usu_nombre in lista_invitados:
    print(f"Bienvenido, {usu_nombre}. Estás en la posición {lista_invitados.index(usu_nombre)+1}")
else:
    print("Lo siento, no estas en la lista")

#9. Manipulación de nombres

u_nombre = input("Introduce tu nombre: ")
u_apellido = input("Introduce tu apellido: ")

alias = u_nombre[:3].lower() + u_apellido[:3].upper()

print(f"Tu alias es {alias}")

#10. Formatear y mostrar datos matemáticos

numero_decimal = float(input("Introduce un número decimal: "))

print(f" El número redondeado es: {round(numero_decimal,2)}")
print(f"El cuadrado es: {numero_decimal**2}")
print(f"La raíz cuadrada es: {numero_decimal**0.5}")