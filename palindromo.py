# Programa para averiguar si una palabra es palindromo o no

#1) crear funcion para revisar la palabra
def palindromo(palabra):
    #Eliminar espacios
    palabra = palabra.replace(' ', '')
    #convertir a minusculas
    palabra = palabra.lower()
    #invertir la palabra
    palabra_invertida = palabra[::-1]
    #si 'palabra' es la misma a la inversa
    if palabra == palabra_invertida:
        return True
    else:
        return False

#2) funcion para mostrarle al usuario el resultado
def run():
    #variable para guardar la palabra
    palabra = input('Escribe una palabra: ')
    #variable para guardar si es o no palindromo
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print (' ES UN PALINDROMO ')
    else:
        print('NO ES PALINDROMO')

#punto de entrada para programa de python
#comienza a correr todo lo que este debajo
if __name__ == '__main__':
    run()