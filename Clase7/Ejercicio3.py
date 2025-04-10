# Ejercicio - Pacman

pos_pacman = int(input("Cúal es la posición de pacman? "))
pos_fantasma = int(input("Cúal es la posición del fantasma? "))

#Comprobamos que la posición sea igual
if pos_pacman == pos_fantasma:
    estado_pacman = input("Cómo está Pacman")
    if estado_pacman == "caramelo"
        print("Pacman se ha comido al fantasma")
    else:
        print("Pacman ha sido atrapado")
else:
    print("Pacman ha escapado")