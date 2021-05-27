def run():
    LIMITE = 1000     #las constantes van en MAYUS
    contador = 0      #definir variable que comenzará en 0 y va a aumentar
    potencia_2 = 2 ** contador

    while potencia_2 < LIMITE:
        print ('2 elevado a ' + str(contador) + 
                'es igual a ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()
