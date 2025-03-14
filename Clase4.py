#ejercicio 1: Operaciones numéricas complejas
#Defines cinco variables numéricas distintas (int, float, complex)
#realiza diversas operaciones matemáticas (potenciación, division entera, módulo)
#imprime los resultados formateados en una cadena clara y descriptiva

#num1 = 5
#num2, num3, num4, num5 = 10, 3, 8.7, 4+2j
#resultado = (f"Potencia: {num1 ** num2}, "
#             f"\nDivisión entera: {num1 // num2}, "
#             f"\nMódulo: {num1 % num2}, "
#             f"\nMultiplicación: {num3 * num4}, "
#             f"\nComplejo: {num5}")
#print(resultado)


#Ejercicio 2: Combinación de cadenas y números
#Define dos variables numéricas (int, float) y tres cadenas diferentes.
# Genera una nueva cadena combinando texto con el resultado de operaciones aritméticas entre estas variables.
# Usa conversión explícita (str()) para insertar valores numéricos en la cadena final.

#num_int, num_float = 8, 3.5
#cadena1, cadena2, cadena3 = "Resultado: ","La suma es: ", "y la división es: "
#resultado = cadena1 + " " + cadena2 + " " + str(num_int + num_float) + " " + cadena3 + " " + str(num_int/num_float)

#print(resultado)

#Ejercicio 3: Manipulación avanzada de cadenas
#Crea una cadena larga que contenga espacios en blanco al inicio, final, y en medio.
# Realiza varias operaciones encadenadas como eliminar
# espacios extremos, covertir to_do a mayúsculas, y dividir la cadena en varias subcadenas usando un separador específico.

#cadena = " Esto es un ejemplo con huecos delante y detrás "
#nueva_cadena = cadena.strip().upper().split()
#print(nueva_cadena)

#Ejercicio 4: Índices y subcadenas
#Define una cadena extensa (mínimo 50 caracteres).
# Obtén varias subcadenas usando la indexación por rangos (slicing) y genera una nueva cadena combinando estas subcadenas en orden inverso.
# Imprime la nueva cadena resultante.

#cadena_extensa = "Python en un lenguaje que me encanta y que me da mucho trabajo."
#subcadena = cadena_extensa[0:6]+ "" + cadena_extensa[11:20] + "" + cadena_extensa [-9:]
#resultado = subcadena[::-1]
#print(resultado)

#Ejercicio 5: Formato y conversión numérica
#Define variables numéricas (entero, flotante, complejo).
# Crea una cadena con formato avanzado (f-strings) que muestre estos números con precisión definida (dos decimales, notación científica, etc.).
# Evita concatenar directamente números y texto.

entero, flotante, complejo = 12, 367.7864574, 5+3j
formato = f"Entero: {entero}, Flotante: {flotante:.2f}, Notación cintífica: {flotante:.2e} , Complejo: {complejo}"
print(formato)
