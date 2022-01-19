#OBJETO
##Agrupacion de datos y metodos que operan en dichos datos

#CLASE
# (molde) Permite crear nuevos tipos que contienen informacion arbitraria sobre un objeto

#INSTANCIA
#Copia especifica de la clae con todo su contenido

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
#Clase para definir la distancia entre coordenadas
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    #metodo-->distancia
    #recibe otra intstancia
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    #crear instancia de la coordenada
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    #print(coord_1.distancia(coord_2))

    #isinstance() --> permite determinar si alguna de las coordenadas es una instanciaa o no de coordenada
    print(isinstance(coord_2, Coordenada))
    ##### // True