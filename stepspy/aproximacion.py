import time

objetivo = int(input('Escoge un numero: '))
# epsilon = 0.0001
epsilon = 0.001
paso = epsilon**2 
respuesta = 0.0
tiempito = time.time()

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
    print(f'El programa demoró { time.time()-tiempito } segundos')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')
    print(f'El programa demoró { time.time()-tiempito } segundos')