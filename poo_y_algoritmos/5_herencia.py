#
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

#SUPERCLASE ES ES RECTANGULO
# la clase CUADRADO extiende a RECTANGULO
class Cuadrado(Rectangulo): 
    def __init__(self, lado):
        #super() --> permite obetener una referencia directa de la superclase (rectangulo)
        #al ejecutar la funcion super(), estamos obteniendo la referencia al rectangulo
        #y podemos llamar a su constructor
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    #se hereda el metodo 'area'
    print(cuadrado.area())
