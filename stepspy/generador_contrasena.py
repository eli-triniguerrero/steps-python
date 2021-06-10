#usando libreria random
import random

def new_password():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z' ]
    chars = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    emoji = ['“ヽ(´▽｀)ノ”', '(*゜▽゜ノノ゛☆', '┐(・。・┐) ♪', '( ง ´◇｀)ง♪', '＼(^o^)／', '（^[]＾）／♪', '≧(´▽｀)≦', '(*￣0￣)θ～♪', 'ヽ(≝∀≝)ﾉ ー♬']

    caracteres = mayus + minus + chars + nums + emoji

    password = []

    for i in range(20):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)
    return password

def run():
    password = new_password()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()