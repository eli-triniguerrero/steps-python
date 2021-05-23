#Conversor de varias monedas

#MENU
# Poner'tres comillas' permite hacer un string
# que considera varias lineas

menu = """
Bienvenido al Conversor de Monedas 💰 
Elige una opción:
1) Peso Colombiano
2) Peso Argentino
3) Peso Mexicano """

opcion = int(input(menu))

if opcion ==1:
    #pass
    #peso colombiano
    pesos = input('¿Cuántos pesos colombianos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print('Tienes $' + dolares + 'dolares')
    #peso argentino
elif opcion == 2:
    pesos = input('¿Cuántos pesos argentinos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print('Tienes $' + dolares + 'dolares')
    #Peso mexicano
elif opcion  == 3:
    pesos = input('¿Cuántos pesos mexicanos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 22
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print('Tienes $' + dolares + 'dolares')
else:
    print('Escribe una opción valida')