class Activity1: 

    #1. Crear método inicializador de la clase
    def _init_(self):
        #2. Declaración de variables
        self.editor_name = 'Visual studio code'
        self.language = 'Python'
        self.version = 3.0

    #3. Método que imprime los valores de las variables
    def show_info(self):
        print(f'Estamos trabajndo en {self.editor_name}, programando en {self.language} {self.version}')

    '''
    Author: Jassy
    Date: 31/08/2022
    Description: python
    '''

    def input_data_user():
        user_name = input('Ingresa tu nombre: ')
        while True: 
            try: 
                age = int(input('Edad: '))
                break
            except: 
                print('Error, no es un valor numérico')
        print(f'{user_name}, tiene {age} años. ')

    '''
    Función 3: solicitud de cantidad de lenguajes de programación
    '''
    def input_frameworks_data():
        while True: 
            try: 
                languages_count = int(input('Cuántos fm conoces?'))
                counter = 1
                while counter <= languages_count: 
                    framework_name = input('     Framework: ')
                    counter += 1
                break
            except: 
                print('Error, no es un valor numerico')

    def input_language_information():
        language_list = []
        while True: 
            try: 
                language_count = int(input('Cuantos lenguajes de programación conoces? '))
                language_list = funcion_ayudante(language_count, language_list)
                break 
            except:
                print('Error, se esperaba un número')

    def funcion_ayudante(language_count, language_list):
        for item_lenguage in range(language_count):
            language_name = input(f'{item_lenguage}, : ')
            language_list.append(language_name)

        return language_list

    def insert_info_student():
        print('Ingresa la siguiente informacoón')
        students_list = []
        while True:
            try:
                student_counter = int(input('Cuántos estudiantes ingresaras? '))

                for item_student in range(1, student_counter+1):
                    student_name = input('      Nombre: ')
                    document = input('    Documento: ')
                    students_list.append((item_student, student_name, document))

                break
            except: 
                print('Error, se esperaba un número')
        

    def countries_information():
    
        countries_list = []
        mayor = 0
        menor = 626959949459

        while True: 
            try: 
                country_counter = int(input('Cuantos paises conoces? '))
                for item_country in range(1, country_counter+1):
                    country_name = input('     Pais:')
                    while True: 
                        try: 
                            population = int(input('      Población: '))
                            break

                        except: 
                            print('Se esperaba un dato númerico')

                    countries_list.append((item_country, country_name, population))
                
                print(f'   Informacion paises\n   {countries_list}') 
                population_mayor(countries_list)
                population_menor(countries_list)
                break

            except: 
                print('Se esperaba un dato númerico')

def population_mayor(countries_list):
    mayor = 0
    actual = crearLista (countries_list)

    for i in range(int(len(actual))):
        if mayor < actual[i]:
            mayor =  actual[i]

    print(f'Población mayor es de: {mayor}')


def population_menor(countries_list):
    menor = 21226595
    actual = crearLista (countries_list)

    for i in range(int(len(actual))):
        if menor > actual[i]:
            menor =  actual[i]

    print(f'Población menor es de: {menor}')

def crearLista (countries_list):
    actual = []

    for i in range(int(len(countries_list))):
        pais_information = countries_list[i]
        actual.append(pais_information[2])
    
    return actual
