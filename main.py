import mysql.connector
import config, requests, temporary_results
import sys
from mysql.connector import Error
from datetime import datetime


def start_program():
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
            print('choice 1')
        elif user_choice == '2':
            print('choice 2')
        elif user_choice == '3':
            print('choice 3')
        elif user_choice == '4':
            print('choice 4')
        elif user_choice == '5':
            print('Выход из программы')
            sys.exit()
    else: 
        print(f'ОШИБКА! "{user_choice}" не соответствует предложенному выбору для ввода!')
        print()
        start_program()


def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
         cursor.close()
         connection.close()
     except Error as err:
         print(f"The error '{err}' occurred")


def show_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         for db in cursor:
             print(db)
         connection.commit()
         print("Query executed succecessfully")
         cursor.close()
         connection.close()
     except Error as err:
         print(f"The error '{err}' occurred")


def show_kinds(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        temporary_results.kinds = []
        for db in cursor:
           print(db)
           temporary_results.kinds.append(db)
        print()
        connection.commit()
        cursor.close()
        connection.close()
    except Error as err:
        print(f"The error '{err}' occurred")


def add_new_animal():

    def istrue(word):
        word = word
        ab = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        if all(sym in ab for sym in word.lower()):
            return True
        else: return False

    def input_name():
        while True:
            name = input('Введите имя животного: ')
            if istrue(name) == True:
                return name
            else: 
                print('Имя должно состоять из букв')
    
    def input_birthday():
        while True:
            mydate = input('Введите дату рождения в формате YYYY-MM-DD: ')
            try:
                valid_date = datetime.strptime(mydate, '%Y-%m-%d').strftime('%Y-%m-%d')
                return valid_date
            except ValueError:
                print('ОШИБКА! Некорректный ввод даты! Введите дату рождения в формате YYYY-MM-DD')
    
    def input_kind():
        what_kinds_in_db = """SELECT id, Title FROM AnimalSpecies""" # запрос к базе данных
        print('Необходимо указать вид животного')
        print('Список доступных видов: ')
        show_kinds(create_connection, what_kinds_in_db)
        while True:
            try:
                kind = int(input('Введите порядковый номер вида: '))
                if 1 <= kind <= len(temporary_results.kinds):
                    return kind
            except ValueError:
                print('Введи число, соответствующее порядковому номеру вида животного!')

    def input_kind():
        what_kinds_in_db = """SELECT id, Title FROM AnimalSpecies""" # запрос к базе данных
        print('Необходимо указать вид животного')
        print('Список доступных видов: ')
        show_kinds(create_connection, what_kinds_in_db)
        while True:
            try:
                kind = int(input('Введите порядковый номер вида: '))
                if 1 <= kind <= len(temporary_results.kinds):
                    return kind
            except ValueError:
                print('Введи число, соответствующее порядковому номеру вида животного!')
    
    animal_name = input_name()
    animal_birthday = input_birthday()
    animal_kind = input_kind()


create_connection = mysql.connector.connect(user=config.user, 
                                            password=config.password,
                                            host=config.host,
                                            port=config.port,
                                            database=config.database)





table_name = 'Animals'

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL, 
  age INTEGER,
  gender TEXT,
  nationality TEXT
)
"""

delete_users_table = """
DROP TABLE users
"""

name = "Dolly"
show_db_query = f"""SELECT Name, Title, Command
                    FROM {table_name}
                    INNER JOIN AnimalSpecies ON Kind = AnimalSpecies.id
                    INNER JOIN Commands ON Commands = Commands.id"""

# show_query(create_connection, show_db_query)
add_new_animal()