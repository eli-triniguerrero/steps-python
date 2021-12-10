# BUSQUEDA BINARIA 
# SE NECESITA UN ORDEN DENTRO DEL CONJUNTO DE BUSQUEDA

# podemos cortad a la mitad cada vez 
objetivo = int(input('Escribe un número: '))
epsilon = 0.01
#limite inferior
bajo = 0.0
#max() arroja el maximo valor entre dos nums
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    #en cada iteracion estamos diviendo entre dos
    respuesta = (alto + bajo) / 2

print(f'La raíz cuadrada de {objetivo} es {respuesta}')

# >>> Escribe un número: 23
#   bajo=0.0, alto=23, respuesta=11.5
#   bajo=0.0, alto=11.5, respuesta=5.75
#   bajo=0.0, alto=5.75, respuesta=2.875
#   bajo=2.875, alto=5.75, respuesta=4.3125
#   bajo=4.3125, alto=5.75, respuesta=5.03125
#   bajo=4.3125, alto=5.03125, respuesta=4.671875
#   bajo=4.671875, alto=5.03125, respuesta=4.8515625
#   bajo=4.671875, alto=4.8515625, respuesta=4.76171875
#   bajo=4.76171875, alto=4.8515625, respuesta=4.806640625
#   bajo=4.76171875, alto=4.806640625, respuesta=4.7841796875
# La raíz cuadrada de 23 es 4.79541015625
