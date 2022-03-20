import random

print("Bienvenido al juego - adivina el numero")

juega = input("Queres jugar el juego? si/no ").lower()
if juega != "si":
    quit()
else: 
    print("bien..juguemos")

num_mayor = input("Ingresa un numero: ")
if num_mayor.isdigit():
    num_mayor = int(num_mayor)

    if num_mayor == 0:
        print("Por favor ingresa un n° mayor a 0")
        quit()
else:
    print("El juego solo funciona con números..saliendo")        

r = random.randint(1, num_mayor)
intentos = 0

while True:
    intentos += 1
    num_usuario = input("Trata de adivinar el numero: ")
    if num_usuario.isdigit():
       num_usuario = int(num_usuario)
    else:
       print("El juego solo funciona con números..ingresa otro")
       continue        

    if num_usuario == r:
        print("Ganaste!!")
        break
    else:
        print("Trata de nuevo!!") 

print("El n° de intentos hasta adivinar fue de", intentos)

           

