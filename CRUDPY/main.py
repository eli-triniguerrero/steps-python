clients = ' pablo, ricardo,'


def create_client(client_name):
#llama a la variable global para usar dentro de la funcion
    global clients

    clients += client_name
    _add_comma


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients

    clients += ','


#punto de entrada
if __name__ == '__main__':
    list_clients()

    create_client('eli')

    print(clients)

    list_clients()