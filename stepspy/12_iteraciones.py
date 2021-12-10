#ITERACIONES (LOOPS)
# CUANDO QUEREMOS QUE UN PROGRAMA HAGA LO MISMO VARIAS VECES, UTILIZAMOS ITERACIONES
# SE PUEDEN ESCRIBIR ITERACIONES DENTRO DE ITERACIONES
# PODEMOS USAR 'BREAK' PARA SALIR ANTICIPADAMENTE DE UNA ITERACIONES

# contador = 0
# while contador < 10:
#     print(contador)
#     contador += 1   # contador = contador +1

#cuando usas WHILE es como si usaras un reloj

# contador_externo = 0
# contador_interno = 0

# while contador_externo < 5:
#     while contador_interno < 6:
#         print(contador_externo, contador_interno)
#         contador_interno += 1
    
#     contador_externo += 1
#     contador_interno = 0

contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >= 3:
            break
    
    contador_externo += 1
    contador_interno = 0