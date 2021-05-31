#crear variable para almacenar el valor de la moneda
pesos = input('¿Cuántos pesos colombiano tienes?: ')
#transformar el valor a numero decimal
pesos = float(pesos)   #convertir a decimal
#crear varible valor pesos
valor_dolar = 21
dolares = pesos / valor_dolar
#la varible redondeamos a 2decimales
dolares = round(dolares,2)
#convertir dolares a texto para imprimirlo en consola
dolares = str(dolares)
#imprimir en pantalla
print('Tienes $' + dolares + 'dolares')