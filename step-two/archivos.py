def read():
    numbers = []
    with open("./archivos/numbers.txt", "r",encoding="utf-8") as f:
        #leer cada linea del archivo
        for line in f:
            numbers.append(int(line))
        print(numbers)

def write():
    names= ['Alejandro','Bethoven', 'Carlos', 'Daniel', 'Eufemio']
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        #recorrer cada elemento de names
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()