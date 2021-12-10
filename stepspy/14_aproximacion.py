# APROXIMACION DE SOLUCIONES
# ALGORITMOS DE APROXIMACION DE SOLUCIONES
# Debemos definir qué tan cerca queremos estar de la solución
# A la diferencia la realidad y la aproximaciones se le llama 'epsilon'

#busar raíz cuadrada
objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

#'abs' regresa valor absoluto

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
# >>> 2.6439**2
# 6.9902072099999994

# >>> Escoge un numero: 2
# ...
# 0.017817590000390293 1.4078999999998614
# 0.01753600000039035 1.4079999999998614
# 0.01725439000039053 1.4080999999998614
# 0.016972760000390608 1.4081999999998613
# 0.016691110000390585 1.4082999999998613
# 0.016409440000390685 1.4083999999998613
# 0.016127750000390684 1.4084999999998613
# 0.015846040000390804 1.4085999999998613
# 0.015564310000390824 1.4086999999998613
# 0.015282560000390966 1.4087999999998613
# 0.015000790000391007 1.4088999999998613
# 0.014719000000390947 1.4089999999998613
# 0.01443719000039101 1.4090999999998612
# 0.014155360000391193 1.4091999999998612
# 0.013873510000391276 1.4092999999998612
# 0.013591640000391259 1.4093999999998612
# 0.013309750000391363 1.4094999999998612
# 0.013027840000391366 1.4095999999998612
# 0.012745910000391492 1.4096999999998612
# 0.012463960000391516 1.4097999999998612
# 0.01218199000039144 1.4098999999998612
# 0.011900000000391486 1.4099999999998611
# 0.011617990000391654 1.4100999999998611
# 0.01133596000039172 1.4101999999998611
# 0.011053910000391687 1.410299999999861
# 0.010771840000391775 1.410399999999861
# 0.010489750000391984 1.410499999999861
# 0.010207640000391871 1.410599999999861
# La raíz cuadrada de 2 es 1.410699999999861

#*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_
# import time

# objetivo = int(input('Escoge un numero: '))
# # epsilon = 0.0001
# epsilon = 0.001
# paso = epsilon**2 
# respuesta = 0.0
# tiempito = time.time()

# while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
#     print(abs(respuesta**2 - objetivo), respuesta)
#     respuesta += paso

# if abs(respuesta**2 - objetivo) >= epsilon:
#     print(f'No se encontro la raiz cuadrada {objetivo}')
#     print(f'El programa demoró { time.time()-tiempito } segundos')
# else:
#     print(f'La raiz cudrada de {objetivo} es {respuesta}')
#     print(f'El programa demoró { time.time()-tiempito } segundos')