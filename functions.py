import temporary_results
from mysql.connector import Error


# Основная функция для выполнения SQL-запросов
def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
         cursor.close()
        #  connection.close()
     except Error as err:
         print(f"The error '{err}' occurred")


# Функция, получающая из базы данных информацию
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
        # connection.close()
    except Error as err:
        print(f"The error '{err}' occurred")


def show_commands(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        temporary_results.commands = []
        for db in cursor:
           print(db)
           temporary_results.commands.append(db)
        print()
        connection.commit()
        cursor.close()
        # connection.close()
    except Error as err:
        print(f"The error '{err}' occurred")