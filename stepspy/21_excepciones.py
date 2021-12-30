#EXCEPCIONES
# Se mpueden manejar con TRY, EXCEPT, FINALLY
# se deben de manejar de manera silencionsa (print estatements)

# def divide_elementos_de_lista(lista, divisor):
#     return [i / divisor for i in lista]

# lista = list(range(10))
# divisor = 2
# print(divide_elementos_de_lista(lista, divisor))
''' // [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5] '''

#cambiar el divisor a 0
# def divide_elementos_de_lista(lista, divisor):
#     return [i / divisor for i in lista]

# lista = list(range(10))
# divisor = 0
# print(divide_elementos_de_lista(lista, divisor))
'''
Traceback (most recent call last):
  File "/Users/trinityhome/Desktop/steps-python/stepspy/21_excepciones.py", line 19, in <module>
    print(divide_elementos_de_lista(lista, divisor))
  File "/Users/trinityhome/Desktop/steps-python/stepspy/21_excepciones.py", line 15, in divide_elementos_de_lista
    return [i / divisor for i in lista]
  File "/Users/trinityhome/Desktop/steps-python/stepspy/21_excepciones.py", line 15, in <listcomp>
    return [i / divisor for i in lista]
ZeroDivisionError: division by zero
 '''

# def divide_elementos_de_lista(lista, divisor):
#     #programacion defensiva
#     try:
#         return [i / divisor for i in lista]
#         #si alguien usa el 0 para dividir, regresa la lista
#     except ZeroDivisionError as e:
#         print(e)
#         return lista

# lista = list(range(10))
# divisor = 0
# print(divide_elementos_de_lista(lista, divisor))
''' // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  '''
''' :::::Cambiando divisor de 0 a 3::::::
    [0.0, 0.3333333333333333, 0.6666666666666666, 1.0, 1.3333333333333333, 1.6666666666666667, 2.0, 2.3333333333333335, 2.6666666666666665, 3.0]
    --------------------------------------------------------
    print(e)--> division by zero
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 '''

#EXCEPCIONES COMO CONTROL DE FLUJO
def busca_pais(paises, pais):
    '''
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    '''    
    try:
        return paises[pais]
    except KeyError:
        #return None
        return print('\n \nTu búsqueda no se encuentra en la base de datos')

paises = {
        'Colombia': 'Bogota',
        'Uruguay': 'Montevideo',
}
pais = 'Mexico'
print(busca_pais(paises, pais))

