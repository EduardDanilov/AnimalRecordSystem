import mysql.connector
import config, sql_requests, temporary_results, functions
import sys
from mysql.connector import Error
from datetime import datetime


def start_program():
    print()
    print('Программа учета животных')
    print('Введите 1, чтобы завести новое животное')
    print('Введите 2, чтобы изменить класс животного')
    print('Введите 3, чтобы вывести полный список животных')
    print('Введите 4, чтобы вывести список команд для выбранного животного')
    print('Введите 5, чтобы выйти из программы')
    print()

    user_choice = input('Сделайте выбор: ')
    if user_choice.isdigit() and 1 <= int(user_choice) <= 5:
        if user_choice == '1':
            add_new_animal()
        elif user_choice == '2':
            print('choice 2')
        elif user_choice == '3':
            show_all_animals()
        elif user_choice == '4':
            print('choice 4')
        elif user_choice == '5':
            print('Выход из программы')
            sys.exit()
    else: 
        print(f'ОШИБКА! "{user_choice}" не соответствует предложенному выбору для ввода!')
        print()
        start_program()


def add_new_animal():
    """Функция добавления нового животного.
       Включает в себя функции добавления и проверки на правильность ввода: 
       - имени, 
       - даты рождения, 
       - вида,
       - выполняемых команд.
    """    
    def input_name():
        while True:
            name = input('Введите имя животного: ')
            if is_true(name) == True: 
                return name
            else: 
                print('Имя должно состоять из букв')
    
    def is_true(word):
        """Функция проверки правильности ввода имени

        Args:
            word (char): поступают введенные пользователем символы

        Returns: Boolean
            True: если в перечне символов (английский и русский алфавиты) встречаются все символы, введенные пользователем
            False: если есть несовпадение в символе
        """        
        word = word
        ab = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        if all(sym in ab for sym in word.lower()):
            return True
        else: return False
    
    def input_birthday():
        while True:
            mydate = input('Введите дату рождения в формате YYYY-MM-DD: ')
            try:
                valid_date = datetime.strptime(mydate, '%Y-%m-%d').strftime('%Y-%m-%d') # Форматирование для вывода даты 
                return valid_date
            except ValueError:
                print('ОШИБКА! Некорректный ввод даты! Введите дату рождения в формате YYYY-MM-DD')
    
    def input_kind():
        """Запросом к базе данных формируется список видов животных, который помещается во временные результаты.
           Далее происходит проверка правильности вводимых данных.

        Returns:
            int: число, соответствующее номеру вида животного
        """        
        what_kinds_in_db = """SELECT id, Title FROM AnimalSpecies""" # Запрос к базе данных
        print('Необходимо указать вид животного')
        print('Список доступных видов: ')
        functions.show_kinds(create_connection, what_kinds_in_db) # Функция отображает список видов, содержащийся в базе данных
        while True:
            try:
                kind = int(input('Введи порядковый номер, соответствующий виду животного: '))
                if 1 <= kind <= len(temporary_results.kinds):
                    return kind
            except ValueError:
                print('Введи число, соответствующее порядковому номеру вида животного!')
    
    def input_commands():
        """Функция отображает команды, выполняемые животными.
           Принцип действия аналогичен функции input_kind() 
        """ 
        what_command_in_db = """SELECT id, Command FROM Commands""" # запрос к базе данных
        print('Можно указать команду, которую выполняет животное')
        print('Список доступных команд: ')
        functions.show_commands(create_connection, what_command_in_db)
        print('Если ничего не выбрал, нажми 0')
        while True:
            try:
                command = int(input('Введите порядковый номер команды: '))
                if 1 <= int(command) <= len(temporary_results.commands):
                    return command
                elif command == 0:
                    return 'NULL'
            except ValueError:
                print('Введи число, соответствующее порядковому номеру команды, или ничего!')

    animal_name = input_name()
    animal_birthday = input_birthday()
    animal_kind = input_kind()
    animal_commands = input_commands()

    sql_request_to_add_new_animal = f"""INSERT INTO Animals (Name, Birthday, Kind, Commands)
                                        VALUES ('{animal_name}', '{animal_birthday}', '{animal_kind}', {animal_commands})"""

    # Непосредственно исполнение функции добавления животного
    functions.execute_query(create_connection, sql_request_to_add_new_animal) 
    
    # Возврат в главное меню
    start_program()


def show_all_animals():
    functions.show_query(create_connection, sql_requests.show_db_query)
    start_program()


create_connection = mysql.connector.connect(user=config.user, 
                                            password=config.password,
                                            host=config.host,
                                            port=config.port,
                                            database=config.database)


start_program()