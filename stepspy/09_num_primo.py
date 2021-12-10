#Programa para determinar si un numero es primo o no

#NUMERO PRIMO: es todo número que puede dividirse
#solamente por sí mismo y por 1

#definir funcion para determinar si el numero es primo
def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

#solicitar el numero al usuario
def run():
    numero = int(input('Hola, escribe un número: ' ))
    if es_primo(numero):
        print(' Tu número ES PRIMO :D')
    else:
        print('Oh, tu número NO ES PRIMO :(')

if __name__ == '__main__':
    run()