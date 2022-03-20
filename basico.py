# Comandos básicos
# escribir por pantalla
print('Hola Mundo', 'Chau Mundo', 'Probano OneLiners', end='|')
print('Nueva Linea')

# leer por pantalla
nombre = input('Nombre: ')
print('El nombre es ' + nombre)

# metódos
hola = 'hola'
print(hola.upper())

chau = 'ChaU'
print(chau.lower().count('a'))

# if/else
x = input('Ingresa tu nombre para comparar: ')

if x == 'pablo':
    print('Bien sos ' + x)
elif x == 'marcos':
    print('ahhh sos marcos')
else:
    print('No sos pablo sos ' +  x)

# Collecciones
# listas (mutables)
x = [4, 'hola', True]
print(len(x))
x.append('chau')
x.extend([3,'agregando', False])
print(x.pop(-1))
print(x[0])

# tuplas (inmutables)
x = (4, 'hola', True)
print(x[2])

# for loops
x = [1,2,3,4]

for i in range(10):
    print(i)

for i in range(10,-1,-1):
    print(i)

for i in ['hola','chau','testing']:
    print(i)

for i, element in enumerate(x):
    print(i, element)        
    
# while loops
i = 0
while i < 10:
    print('numero ' + str(i))
    i += 1

# sets (no importa el orden)    
x = {1,2,3,4,4}
x.add(5)
x.remove(1)
print(2 in x)
print(x)   

# funciones
def funcion(x, y):
    print('Esto es una funcion ' + x + y)

funcion('de',' prueba')    

