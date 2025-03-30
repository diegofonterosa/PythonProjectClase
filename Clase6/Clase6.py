#1.Crear una lista con los días de la semana y mostrar el primer y último día.

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print("Primer día de la semana: ", dias[0])
print("Primer día de la semana: ", dias[-1])

#2.Modificar un elemento de una lista de frutas y agregar una fruta nueva al final.

frutas = ["Manzana", "Platano", "Pera"]
frutas[0]="Mango"
print(frutas)
#Añado una fruta al final
frutas.append("Sandia")
print(frutas)

#3.Crear una lista vacía y llenarla con tres colores usando append().

colores = []
print(colores)
colores.append("Rojo")
colores.append("Amarillo")
colores.append("Rojo")
print(colores)

#4.Ordenar una lista de números desordenados y mostrarla al revés.

numeros = [6,2,4,0,1,12,6,8]
#ordenarlos
numeros.sort()
print(numeros)
#Invierto el orden
numeros.reverse()
print(numeros)

#5.Eliminar un elemento de una lista y mostrar el resultado.

animales = ["Perro", "Pulpo", "Gato", "Rinoceronte"]
print(animales)
animales.remove("Gato")
print(animales)

#6.Contar cuántas veces aparece un número en una lista.

numeritos = [4,6,7,8,2,3,4,5,6,7,8,9]
cantidad = numeritos.count(4)
print("El numero de veces que se repite el numero es: ", cantidad)

#7.Crear una tupla con tres elementos de distinto tipo y mostrar cada uno.

mi_tupla = (19, "Mario", True)
print("Numero: ", mi_tupla[0])
print("String: ", mi_tupla[1])
print("Boolean: ", mi_tupla[2])

#8.Acceder al segundo elemento de una tupla anidada dentro de una lista.

datos = ["Nombre", (100,200), "Apellido"]
tupla_intermedia = datos[1]
print(tupla_intermedia)

#9.Desempaquetar una tupla en tres variables y mostrarlas con print().

persona = ("Sara", 32, "Madrid")
nombre, edad, ciudad = persona
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Ciudad: ", ciudad)

#10.Crear una lista con nombres de alumnos, cambiar el nombre del segundo y mostrar la lista completa.
