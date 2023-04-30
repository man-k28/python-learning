#todo: Реализовать класс враппер PgDataBase над библиотекой psycopg3.
# предусмотреть методы
# __connect()
# create_database
# insert(sql, data)
# select(sql)
# delete(sql)
# update(sql, data)
# close_database()

import psycopg


class PgDataBase:
    __db = psycopg

    def connect(self, connect_str: str = ''):
        return self.__db.connect(connect_str)

    @staticmethod
    def create_database(sql: psycopg.Connection.connect):
        with sql.cursor() as cur:
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS test (
                    id serial PRIMARY KEY,
                    data text)
                """)
            sql.commit()

    @staticmethod
    def insert(sql: psycopg.Connection.connect, data):
        with sql.cursor() as cur:
            cur.execute(f'INSERT INTO test (data) VALUES (\'{data}\')')
        sql.commit()

    @staticmethod
    def select(sql: psycopg.Connection.connect):
        with sql.cursor() as cur:
            cur.execute("SELECT * FROM test")
            return cur

    @staticmethod
    def delete(sql: psycopg.Connection.connect):
        with sql.cursor() as cur:
            cur.execute(f'DELETE FROM test')
        sql.commit()

    @staticmethod
    def update(sql: psycopg.Connection.connect, data, index):
        with sql.cursor() as cur:
            cur.execute(f'UPDATE test SET data = \'{data}\' WHERE id = {index}')
        sql.commit()

    @staticmethod
    def close_database(sql: psycopg.Connection.connect):
        sql.close()


if __name__ == "__main__":
    try:
        database = PgDataBase()
        conn = database.connect('user=postgres password=postgres')
        database.create_database(conn)
        database.insert(conn, 'test_data')

        database.delete(conn)
        database.close_database(conn)
    except Exception as e:
        print(e)
