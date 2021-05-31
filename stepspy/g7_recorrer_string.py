#programa para recorrer un string con ciclo FOR
def run():
    #pedir al usuario que escriba una palabra
    palabra = input('Hola Usuario, escribe una palabra: ')
    #recorrer esa palabra
    for letra in palabra:
        print(letra)

if __name__ == '__main__':
    run()