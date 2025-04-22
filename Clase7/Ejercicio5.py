# Ejercicio 5 - Puede entrar en el servidor de Discord?

rol = input("Dime el rol del usuario: ")
academia = input("En que academia estudias/trabajas? ")

if rol == "alumno" and academia == "Prometeo":
    print("Acceso al servidor de Discord oficial y extraoficial")
elif rol == "profesor" and academia == "Prometeo":
    print("Acceso al Discord oficial")
else:
    print("No tienes acceso al servidor de Discord")
