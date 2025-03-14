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
# espacios extremos,


cadena = " Esto es un ejemplo con huecos delante y detrás "
nueva_cadena = cadena.strip().upper().split()
print(nueva_cadena)