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

    def execute(self, query):
        with self.__conn__.cursor() as cur:
            cur.execute(query)
            return cur

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
        self.execute(open("create_database.sql", "r").read())
        self.execute(open("content.sql", "r").read())

    def list_countries(self):
        with self.__conn__.cursor() as cur:
            cur.execute('Select * from country')
            for val in cur.fetchall():
                print(f'[{val[0]}] - {val[1]}')

    def list_cities(self):
        with self.__conn__.cursor() as cur:
            cur.execute('Select * from city')
            for val in cur.fetchall():
                print(f'[{val[0]}] - {val[1]}')

    def list_permit(self, country):
        with self.__conn__.cursor() as cur:
            cur.execute(f'Select permit.id, cost, rating, country.name, city.name from permit JOIN city ON '
                        f'city.id = city JOIN country ON city.country = country.id WHERE country.name = \'{country}\'')
            for val in cur.fetchall():
                cur.execute(f'select entertainment.name from entertainment_permit join entertainment ON '
                            f'entertainment.id = entertainment_permit.entertainment where permit = {val[0]}')
                entertainments = []
                for ente in cur.fetchall():
                    entertainments.append(ente[0])
                print(f'[{val[0]}] - Цена: {val[1]}, рейтинг: {val[2]}, страна: {val[3]}, город: {val[4]}, развлечения: {"-".join(entertainments)}')

    def list_top_permit(self):
        with self.__conn__.cursor() as cur:
            cur.execute(f'Select permit.id, cost, rating, country.name, city.name from permit JOIN city ON '
                        f'city.id = city JOIN country ON city.country = country.id where rating > 7')
            for val in cur.fetchall():
                cur.execute(f'select entertainment.name from entertainment_permit join entertainment ON '
                            f'entertainment.id = entertainment_permit.entertainment where permit = {val[0]}')
                entertainments = []
                for ente in cur.fetchall():
                    entertainments.append(ente[0])

                print(f'[{val[0]}] - Цена: {val[1]}, рейтинг: {val[2]}, страна: {val[3]}, город: {val[4]}, развлечения: {"-".join(entertainments)}')

    def buy_permit(self, index):
        with self.__conn__.cursor() as cur:
            cur.execute(f'Select permit.id, cost, rating, country.name, city.name from permit JOIN city ON '
                        f'city.id = city JOIN country ON city.country = country.id WHERE permit.id = {index}')
            print("Do you have childrens less 12 year [y/n]")
            y = input()

            discount = 1

            if y == 'y':
                discount = 0.95

            for val in cur.fetchall():
                print(f'[{val[0]}] - Цена: {val[1] * discount}, рейтинг: {val[2]}, страна: {val[3]}, город: {val[4]}')


if __name__ == "__main__":
    db = DB().get_instance()
    try:
        db.connect("127.0.0.1", 5432, "turist", "postgres", "postgres")
        db.init_database()
        while(True):
            print("Select of option:\n[1] - list all countries\n[2] - list all cities\n"
                  "[3] - list all permit. [county]\n[4] - list top permit.\n[5] - exit")
            x = input()

            def buy_by_index():
                print("Select permit:")
                y = input()
                db.buy_permit(int(y))
                print("Your are buy permit")

            x_splitted = x.split(' ')

            if len(x_splitted) > 1 and int(x_splitted[0]) == 3:
                db.list_permit(x_splitted[1])
                buy_by_index()
            elif int(x) == 1:
                db.list_countries()
            elif int(x) == 2:
                db.list_cities()
            elif int(x) == 4:
                db.list_top_permit()
                buy_by_index()
            else:
                break

    except Exception as e:
        print("Error of database: ", e)
    else:
        db.close()
