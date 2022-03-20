print("Bienvenido al juego - preguntas y respuestas")

juega = input("Queres jugar el juego? si/no ").lower()
if juega != "si":
    quit()
else: 
    print("bien..juguemos")

puntaje = 0

preg = input("que significa CPU? ").lower()
if preg == "unidad central de procesamiento":
    print("Correcto")
    puntaje +=1
else: 
    print("Incorrecto!!!")

preg = input("que significa GPU? ").lower()
if preg == "unidad de procesamiento grafico":
    print("Correcto")
    puntaje +=1
else: 
    print("Incorrecto!!!")

preg = input("que significa RAM? ").lower()
if preg == "memoria de acceso aleatoria":
    print("Correcto")
    puntaje +=1
else: 
    print("Incorrecto!!!")         

preg = input("que significa PSU? ").lower()
if preg == "fuente de alimentacion":
    print("Correcto")
    puntaje +=1
else: 
    print("Incorrecto!!!")

print("El puntaje total de respuestas correctas es", puntaje)
print("El porcentaje total de respuestas correctas es", puntaje/4 * 100, "%")