def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
        num = input('Ingresa un número: ')
        # isnumeric devuelve TRUE si corresponde a numero
        #assert: exp que si es TRUE permite seguir con el código, si es FALSE , termina
        assert num.isnumeric(), 'Debes ingresar un número XD'
        print(divisors(int(num)))
        print("Terminó mi programa")


if __name__ == '__main__':
    run()