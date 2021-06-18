# imprimir los primeros 100 numeros elevados al cuadrado
# def run():
#     squares = []
#     for i in range(1,101):
#         squares.append(i**2)
    
#     print(squares)

#que no sean divisibles entre 3
# def run():
#     squares = []
#     for i in range(1,101):
#         if i % 3 != 0:
#             squares.append(i**2)
    
    #print(squares)

#list comprehensions
# def run():
#     squares = [i**2 for i in range(1, 101) if i % 3 !=0]

#     print(squares)

#CREAR UN LIST COMPREHENSION, UNA LISTA DE TODOS LOS MULTIPLOS DE 4
# QUE A LA VEZ TAMBIÉN SON MULTIPLOS DE 6 Y DE 9
# HASTA 5 DIGITOS
def run():
    squares_four = [i**2 for i in range(1,101) if i % 4 != 0]
    squares_six = [i**2 for i in range(1,101) if i % 6 != 0]
    squares_nine = [i** 2 for i in range(1,101) if i %9 != 0]

    print(f'multiplo de 4')
    print(squares_four) 
    print(f'multiplo de 6')
    print(squares_six)
    print(f'multiplo de 9')
    print(squares_nine)
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
    squares = [i**2 for i in range(1,101) if i % 4 != 0 and i % 6 != 0 and i % 9 != 0]
    print(f'MULTIPLOS DE 4, 6, 9')
    print(squares)
 #-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-   
    cuadrado = [i**2 for i in range(1,101) if i % 25 != 0]
    print(f'MULTIPLOS DE 4, 6, 9')
    print(cuadrado)
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

def lista():
     squares = [i for i in range(1,1000000) if i % 36 == 0 and len(str(i)) < 6]





if __name__ == '__main__':
    run()
    list()