#Crear un programa que permita adivinar 
#el numero secreto de la computadora.
#Si adivina el usuario, imprimir WIN
#si no adivina imprimir ES MAS GRANDE o MAS PEQUEÑO

#modulo de python
#paquete de codigo para ejecutar cositas
import random

def run():
    #turno de la compu
    num_aleatorio = random.randint(1, 100)
    num_elegido = int(input('Hola! Adivina el número que estoy pensando 🤭 : '))
    while num_elegido != num_aleatorio:
        if num_elegido < num_aleatorio:
            print('busca un número más GRANDE 👍🏼 ')
        else:
            print('busca un número más pequeño 👎🏼 ')
        num_elegido = int(input('Escribe otro número 😬: '))
    print('⭐️⭐️⭐️⭐️⭐️ G A N A S T E ⭐️⭐️⭐️⭐️⭐️')

if __name__ == '__main__':
    run()