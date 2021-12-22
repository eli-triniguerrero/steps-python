# #FACTORIAL:
# El factorial de un número entero positivo ( 0,1,2,3,4,5,6,...)
# es el producto de todos los enteros positivos
# desde 1 hasta él. !

# n! = n * (n - 1)!

# 5! = 1 * 2 * 3 * 4 * 5 = 120

#Ejemplo:
# 3! = 3 * 2 * 1 = 6
# '6' es el núm de combinaciones que tendría un grupo de '3' elementos

def factorial(n):
    """ Calcular el factorial de n.
    n int > 0
    returns n!
    """
    print(n)
    #escribir caso base
    if n == 1 :
        return 1

    return n * factorial(n - 1)

n = int(input('Escribe un entero: '))

print(factorial(n))