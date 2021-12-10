# preguntar al usuario por dos numeros y compararlo
num_1 = int(input('Escribe un número: '))
num_2 = int(input('Escribe otro número: '))

if num_1 > num_2:
    print('El NUM1 es mayor que el segundo')
elif num_1 < num_2:
    print('El NUM2 es mayor que el primero')
else:
    print('Los números son iguales')