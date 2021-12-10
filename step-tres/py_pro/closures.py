# La funcion tiene que llamarse en la nested 
# para que la funcion decorador pueda incluirla. 
# Sin la nested tendriamos que llamar a la funcion 
# decorador e incluirle la funcion hola. 
# Con este sistema solo creamos el decorador 
# con nested y lo colocamos como decorador 
# en la funcion que queremos decorar.

# hola 3 -> holaholahola

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Sólo puedes utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola "))

    repeat_10 = make_repeater_of(10)
    print(repeat_10("Eli"))

if __name__ == '__main__':
    run()