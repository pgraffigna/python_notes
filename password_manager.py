master_pwd = input("Ingresa el master password: ")

def agregar():
    nombre = input("Ingresa tu nombre: ")
    pwd = input("Ingresa tu password: ")

    with open('passwords.txt', 'a') as f:
        f.write(nombre + ":" + pwd + "\n") 

def ver():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
    
while True:
    modo = input("Queres agregar un nuevo password o ver los existentes? A (agregar), V (ver), apreta S para salir: ").lower()
    if modo == "s":
        break
    
    if modo == "v":
        ver()        
    elif modo == "a":
        agregar()  
    else:
        print("Modo incorrecto!!")
        continue

