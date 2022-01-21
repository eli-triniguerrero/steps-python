#
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Ando, ando, caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        #inicializar la superclase / tener refe
        super().__init__(nombre)

    def avanzar(self):
        print('Ando en mi bicicleta :D')


def main():
    persona = Persona('Elizabeth')
    persona.avanzar()

    ciclista = Ciclista('Sherlock')
    ciclista.avanzar()

    

if __name__ == '__main__':
    main()