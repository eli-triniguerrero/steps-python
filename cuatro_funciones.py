#funciones : reutilizar codigo
# def imprimir_mensaje():
#     print('Mensaje secreto')
#     print('Mi mensaje secreto es screto x.x ')

# imprimir_mensaje()

#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

#Funcion con parametro
def mensaje(msg):
    print('Hola')
    print('Consola 🖥')
    print(msg)
    print('EXIT')

opcion = int(input('Elige una opcion (1, 2, 3): '))
if opcion == 1:
    mensaje('Elegiste el número 1')
elif opcion == 2:
    mensaje('Elegiste el número 2')
else:
    print('Error, escribe una opción correcta')
