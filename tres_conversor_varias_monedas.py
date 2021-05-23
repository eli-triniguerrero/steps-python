#Conversor de varias monedas

#MENU
# Poner'tres comillas' permite hacer un string
# que considera varias lineas

#agregando funcion conversor
def conversor (tipo_peso, valor_dolar):
    pesos = input('¿Cuántos pesos ' + tipo_peso + 'tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print('Tienes $' + dolares + 'dolares')

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
    conversor("colombianos", 3875)    
    #peso argentino
elif opcion == 2:
    conversor('argentinos', 65)
    #Peso mexicano
elif opcion  == 3:
    conversor('mexicanos', 23)
else:
    print('Escribe una opción valida')