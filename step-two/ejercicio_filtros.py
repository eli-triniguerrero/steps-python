#lista de diccionarios
DATA = [
    {
        'name': 'Alejandro',
        'age': 72,
        'organization': 'Google',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Google',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Google',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Google',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #mostrar solo los que programan rn python
    #all_python_devs = [worker['name'] for worker in DATA if worker["language"] == "python"]
    #usando filter y map
    all_python_devs = list(filter(lambda worker:worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))

    #todos los trabajadores en google
    #all_google_workers = [worker['name'] for worker in DATA if worker['organization'] == "Google"]
    #usando filter y map
    all_google_workers = list(filter(lambda worker:worker['organization'] == 'Google', DATA))
    all_google_workers = list(map(lambda worker: worker['name'], all_google_workers))

    #los mayores
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))

    #agregarle una llave mas 
    #el list transforma el resultado que genera 'map', 
    #en un diccionario nuevo con uno nuevo, la llave 'old
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))




    for worker in all_google_workers:
        print(worker)


if __name__ == '__main__':
    run()