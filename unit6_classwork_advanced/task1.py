#todo:
# Организовать подключение к DB Postgres на базе паттерна Singleton
# Использовать библиотеку https://www.psycopg.org/psycopg3/docs/basic/index.html
# Пароли спросить у админа.
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
        self.__conn__ = psycopg.connect(f'host={ip} port={port} dbname={database} user={user} password={password}')
        with self.__conn__.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS test (
                    id serial PRIMARY KEY,
                    data text)
                """)
        self.__conn__.commit()

    def close(self):
        self.__conn__.close()


if __name__ == "__main__":
    db = DB().get_instance()
    try:
        db.connect("127.0.0.1", 5432, "postgres", "postgres", "123")
    except Exception as e:
        print("Error of database: ", e)
    else:
        db.close()
