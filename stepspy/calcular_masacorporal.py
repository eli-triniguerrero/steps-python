#ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO 
# SU PESO EN KG Y ESTATURA EN METROS
#CALCULE EL INDICE DE MASA CORPORAL Y LO ALMACENE EN UNA VARIABLE, 
# Y MUESTRE POR PANTALLA LA FRASE : "TU INDICE DE MASA CORPORA ES <IMC>"
#DONDE <IMC> ES EL INDICE DE MASA CORPORAL CALCULADO REDONDEADO CON DOS DECIMALES

#IMC = PESO KG / ESTATURA AL CUADRADO
def run():
    estatura_mt = float(input('📝 Vamo a calcular tu Indice de Masa Corporal. ¿Cuánto mides?📏'))
    peso_kg = float(input('¿Cuál es tu peso?⚖️'))
    imc = round(peso_kg / estatura_mt * estatura_mt, 2)
    if imc < 18.0:
        print('Tu índice de masa corporal es ' + str(imc) + '. Toma esta cena 🍜🍛🍖🥗 para que no te desmayes! 😜')
    elif imc > 18.1 and imc < 25.0:
        print('Tu índice de masa corporal es ' + str(imc) + '. Ni muy muy ni tan tan! Estas cool!! Toma, un ensalada 🥗 y sonríe 😁') 
    elif imc >25.1 and imc < 29.9:
        print('Tu índice de masa corporal es ' + str(imc) +'. Solo estas pasadito de la media. Toma un chanwis 🥪')
    elif imc >= 30.0:
        print('Tu índice de masa corporal es ' + str(imc) +'. Me parece que ví un lindo puerquito 🐷 ¡Te pasaste de tamales!🐷')
    else:
        return False

if __name__ == '__main__':
    run()