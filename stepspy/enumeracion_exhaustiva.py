#determinar si un numero tiene raiz cuadrada

import time

objetivo = int(input('Escribe un número: '))
respuesta = 0
tiempo_inicial = time.time()
#mientras respuesta al cuadrado sea menor que objetivo
#respuesta aumenta en 1
while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de { objetivo } es { respuesta }')
else:
    print(f'{ objetivo } no tiene raíz exacta')

print(f'El programa demoró { time.time()-tiempo_inicial } segundos')
