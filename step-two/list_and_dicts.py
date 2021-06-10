def run():
    #lista
    my_list = [1, 'holi', True, 4.5]
    #diccionario
    my_dict = {'firstname': 'Trinitron', 'lastname': 'Warrior'}
    #lista que contiene diccionarios
    super_list = [
        {'firstname': 'Alejandro', 'lastname': 'Fernández'},
        {'firstname': 'Enrique', 'lastname': 'Iglesias'},
        {'firstname': 'Carlos', 'lastname': 'Santana'},
        {'firstname': 'Bob', 'lastname': 'Marley'},
    ]
    #diccionario con varias listas
    #cada llave tiene su valor, y cada valor corresponde a su vez a una lista
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.2, 3.3, 4.4, 5.5]
    }
    #recorrer super diccionario
    for key, value in super_dict.items():
        print(key, "-", value)

    for person in super_list:
        print(person['firstname'])
    
    for last in super_list:
        print(last['lastname'])
    
    


if __name__ == '__main__':
    run()