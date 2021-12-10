#tiempo que tarda en ejectuarse la funcion en pantalla

from datetime import datetime

def execution_time(func):
    #" no importa la cant de argumentos nombrados, se deben recibir
    #args: arguments | kwargs: key arguments
    def wraper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + "segundos")
    return wraper

@execution_time
def random_func():
    #Cuando se coloca un _(guionbajo) despues del FOR indica que no interesa por el momento la variable
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre = "Tita"):
    print("Hola" + nombre)


random_func()
suma(5,5)
saludo("Elizabeth")


