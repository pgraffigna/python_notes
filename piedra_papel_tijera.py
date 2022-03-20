import opcode
import random

print("Bienvenido al juego - piedra papel o tijera")

juega = input("Queres jugar el juego? si/no ").lower()
if juega != "si":
    quit()
else: 
    print("bien..juguemos")

puntos_us = 0
puntos_com = 0
opciones =  ["piedra", "papel", "tijera"]

while True:
    eleccion_us = input("Ingresa piedra/papel/tijera o S para salir: ").lower()
    if eleccion_us == "s":
        break

    if eleccion_us not in opciones:
        print("Por favor ingresa las opciones correctas!!")
        continue

    r = random.randint(0,2)
    eleccion_com = opciones[r]
    print("La compu eligio: ",eleccion_com)

    if eleccion_us == "piedra" and eleccion_com == "tijera":
        print("Ganaste un punto!!!")
        puntos_us +=1
        
    elif eleccion_us == "papel" and eleccion_com == "piedra":
        print("Ganaste un punto!!!")
        puntos_us +=1
        
    elif eleccion_us == "tijera" and eleccion_com == "papel":
        print("Ganaste un punto!!!")
        puntos_us +=1
        
    else:
        print("Perdiste!!")
        puntos_com +=1
        
print("El puntaje final para el usuario es: ",puntos_us)
print("El puntaje final para la compu es: ",puntos_com)
print("Termino el juego")
