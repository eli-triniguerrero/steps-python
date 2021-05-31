#interrumpir ciclos usando BREAK y CONTINUE

def run():
    #para el contador en el rango...
    #for contador in range(1000):
        #si contador modulo2 es distinto a 0, va a continuar
        #al dividirlo entre dos el resto es distinto a 0
    #    if contador %2 != 0:
    #        continue
    #    print(contador)

    #for i in range (10000):
        #print(i)
    #    if i == 5500:
            #cortar ciclo
    #        break

    texto = input('Escribe un texto: ')
    for letra in texto:
            if letra == 'o':
                break
            print(letra)

if __name__ == '__main__':
    run()