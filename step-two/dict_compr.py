def run():
    #my_dict={}

    # for i in range(1,101):
    #    if i % 3 != 0:
    #     my_dict[i] = i**3

    # my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0 }

#CREAR CON UN DICTIONARY COMPREHENSION
#UN DICCIONARIO CUYAS LLAVES SEAN LOS 1000
#PRIMEROS NUMEROS NATURALES CON SUS RAICES CUADRADAS COMO VALORES
    my_dict = {i : round(i**0.5,3) for i in  range(1,1001)}
    print(my_dict)  




if __name__ == '__main__':
    run()