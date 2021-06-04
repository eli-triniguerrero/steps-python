#PROGRAMA QUE SOLICITE LA EDAD DE DOS USUARIOS 
#COMPARA LAS EDADES E IMPRIME EN PANTALLA QUIEN ES EL MAYO DE LOS DOS

def run():
    print("""VAMO A JUGAL 
    Hola, Persona,
    🦾👽 soy la Consola 
    """)
    persona_uno = input('¿Cómo te llamas?👁')
    edad_uno = int(input('¿Cuántos años tienes?'))
    print("""pst, pst)) 
    Hola,Segunda Persona,
    🦾👽 soy la Consola 
    """)
    persona_dos = input('¿Cuál es tu nombre?👁')
    edad_dos = int(input('¿Cuál es tu edad?'))
    if edad_uno > edad_dos:
        print('🔮¡CHISPAS!🔮')
        print(persona_uno + ' es mayor que tú, ' + persona_dos)
    elif edad_uno < edad_dos:
        print('🔮¡CHISPAS!🔮')
        print(persona_dos + ' es mayor que tú, ' + persona_uno)
    else:
        print('🔮¡CHISPAS!🔮')
        print(persona_uno + ' y tú, ' + persona_dos + ' tienen la misma edad ! ')
    pass


if __name__ == '__main__':
    run()