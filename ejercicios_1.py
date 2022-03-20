"""1 - definir una funcion que tome como argumento dos numeros
   y devuelva el mayor de ellos"""

def max(num1,num2):
    if num1 > num2:
        print("el numero mayor es", num1)
    else:
        print("el numero mayor es", num2)

# usando max()
def mayor(num1,num2):
    max(num1,num2)

def f_max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2                

max(9,5)
mayor(3,2)
print(f_max(4,2))

"""2 - definir una funcion que tome 3 argumentos y devuelva el mayor de ellos"""

def max_de_tres(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(max_de_tres(1,2,0))            

"""3 - Definir una función que calcule la longitud de una lista o una cadena dada"""

# sin len()
def calc_len():
    cadena = input("ingresa una palabra: ")
    letras = 0 
    for i in cadena:
        letras += 1
    print(letras)
    
calc_len()    

"""4 -  Escribir una función que tome un carácter y devuelva True si es una vocal
de lo contrario devuelve False"""

def char_true(letra):
    if letra in "aeiou": print("True")
    else: print("False")

# usando lista
def char_true(letra):
    vocales = ['a','e','i','o','u']
    if letra in vocales: return True
    else: return False
    
print(char_true("z"))

"""5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
 Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24"""

def sum(lista):
    res = 0
    for i in lista:
        res = res + i
    print(res)

sum([1,2,3,4])    

def multi(lista):
    res = 1
    for i in lista:
        res = res * i
    print(res)

multi([1,2,3,4])

"""6 - Definir una función inversa() que calcule la inversión de una cadena"""

def inversa():
    cadenas = "estoy probando"[::-1]
    return cadenas

print(inversa())

"""7 - Definir una función es_palindromo() que reconoce palíndromos
  ejemplo: es_palindromo ("radar") tendría que devolver True"""

def es_palindromo():
    cadena_pal = input("Ingresa una palabra: ")
    if cadena_pal[::1] == cadena_pal[::-1]: return True
    else: return False    

print(es_palindromo())

"""8 - Definir una función superposicion() que tome dos listas 
y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado"""

def superposicion():
    for i in [1, 2, 3]:
        for j in [1, 4, 5]:
            if i == j:
                print(f"las dos listas coinciden en el número {i}")
            
superposicion()

"""9 - Definir una función generar_n_caracteres() que tome un entero n 
y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"""

def generar_n_caracteres(n1, c1):
    print(int(n1) * c1)

generar_n_caracteres(10, "x")

"""10 - Definir un histograma procedimiento() que tome una lista de números enteros 
e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) 
debería imprimir lo siguiente: **** ********* *******"""

def procedimiento():
    for i in [4, 9, 7]:
        print(f"*" * int(i))

procedimiento()        