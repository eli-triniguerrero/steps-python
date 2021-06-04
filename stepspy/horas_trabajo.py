#ESCRIBIR UN PROGRAMA QUE PREGUNTE AL USUARIO 
# POR EL NUMERO DE HORAS TRABAJADAS Y COSTO POR HORA
#DESPUES, MOSTRAR  EN PANTALLA LA PAGA QUE LE CORRESPONDE

def run():
    trabajador_horas = int(input('Hola, ¿cuántas horas trabajaste?: '))
    costo_hora = int(input('¿Cuánto cuesta una hora?: '))
    sueldo = trabajador_horas * costo_hora
    print('Tu sueldo total es de $ ' + str(sueldo)) 

if __name__ == '__main__':
    run()