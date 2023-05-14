# todo:
#  БД "Система проверки задач"
# Описание предметной области. БД создается для информационного обслуживания учебного процесса.
# Преподаватель каждый урок выдает некоторое количество задач в качестве домашнего задания.
# Каждый ученик решает задачи и переводит ее в статус решенную выкладывая ее на Git
# Система, забирает задачу с Git'а и проверяет каждую задачу прогоняя ее через тесты и запуская ее в виртульном окружении
# и либо подтверждает ее статус как решенную либо возвращает сообщение об ошибки ( меняя ее статус как не решенную.)
#
#
# Разработайте систему с учетом бизнес сущностей:
# Группа, Преподаватель, Студент, Занятие, Задача
#
# Запросы:
# 1. Выдавать список задач по категории (категориями являются темы занятий)
# 2. Выдавать список задач по уровню сложности
# 3. Выдавать список решенных и не решенных задач для слушателя
# 4. Выдавать весь список задач выданный слушателю
# 5. Выдавать список группы по преподавателю
# 6. Предусмотреть возможность изменения статуса задачи для конкретного слушателя
# 7. Выдавать процент решенных задач. (Соотношение между общим кол-вом и решенным)
# 8. Выдавать процент успеваемости по всей группе.
from enum import auto

# Система:
# 1. Написать утилиту которая генерирует файлы taskN.py в папке classwork по номеру задачи.
# Задачи все храняться в БД.

import psycopg


class DB:
    __instance__ = None
    __conn__ = None

    def __init__(self):
        if DB.__instance__ is None:
            DB.__instance__ = self
        else:
            raise Exception("We can not creat another class")

    @staticmethod
    def get_instance():
        if not DB.__instance__:
            DB()
        return DB.__instance__

    def connect(self, ip, port, database, user, password):
        base_conn = psycopg.connect(f'host={ip} port={port} dbname=postgres user={user} password={password}',
                                    autocommit=True)
        with base_conn.cursor() as cur:
            cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{database}'")
            db_exist = cur.fetchall()
            if len(db_exist) == 1:
                cur.execute(f"""DROP DATABASE IF EXISTS {database}""")
            cur.execute(f"""
                CREATE DATABASE {database}
                    WITH
                    OWNER = {user}
                    ENCODING = 'UTF8'
                    LC_COLLATE = 'ru_RU.UTF-8'
                    LC_CTYPE = 'ru_RU.UTF-8'
                    TABLESPACE = pg_default
                    CONNECTION LIMIT = -1
                    IS_TEMPLATE = False
                """)

        self.__conn__ = psycopg.connect(f'host={ip} port={port} dbname={database} user={user} password={password}',
                                        autocommit=True)

    def close(self):
        self.__conn__.close()

    def init_database(self):
        with self.__conn__.cursor() as cursor:
            cursor.execute(open("create_database.sql", "r").read())
            cursor.execute(open("content.sql", "r").read())


if __name__ == "__main__":
    db = DB().get_instance()
    try:
        db.connect("127.0.0.1", 5432, "styding", "postgres", "postgres")
        db.init_database()
    except Exception as e:
        print("Error of database: ", e)
    else:
        db.close()
