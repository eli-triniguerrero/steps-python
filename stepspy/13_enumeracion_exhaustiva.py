# ENUMERACIÓN EXHAUSTIVA
# ENUMERAR TODAS LAS POSIBILIDADES

#determinar si un numero tiene raiz cuadrada
objetivo = int(input('Escribe un número: '))
respuesta = 0

#mientras la respuesta al cuadrado sea menor al objetivo, 
# #va aumentar la respuesta en 1

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raiz cuadrada exacta')

# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_

# import time

# objetivo = int(input('Escribe un número: '))
# respuesta = 0
# tiempo_inicial = time.time()
# #mientras respuesta al cuadrado sea menor que objetivo
# #respuesta aumenta en 1
# while respuesta**2 < objetivo:
#     print(respuesta)
#     respuesta += 1

# if respuesta**2 == objetivo:
#     print(f'La raíz cuadrada de { objetivo } es { respuesta }')
# else:
#     print(f'{ objetivo } no tiene raíz exacta')

# print(f'El programa demoró { time.time()-tiempo_inicial } segundos')
