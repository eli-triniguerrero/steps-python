class Lavadora:

    def __init__(self):
        pass

    #metodo publico: LAVAR
    #llama a metodos privados que no interesan al usuario
    def lavar(self, temperatura='caliente'):
        #ciclo de lavado
        self._llenar_tanque_de_agua(temperatura)
        self._agregar_jabon()
        self._lavar()
        self._centrifugar()

    #definir qué significa llenar el tanque de agua
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')
    #definir agregar jabon
    def _agregar_jabon(self):
        print('Agregando jabón ... ')
    
    def _lavar(self):
        print('<<lavando ropa>>')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()

