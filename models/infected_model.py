import pymysql.cursors


class Infected:
    def __init__(self, id, name, graveyard, city):
        self.id = id
        self.name = name
        self.graveyard = graveyard
        self.city = city

    @staticmethod
    def select_infected():
        connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', cursorclass=pymysql.cursors.DictCursor)

        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ID, NAME, GRAVEYARD, CITY FROM INFECTED")
            results = list(cursor.fetchall())

            cursor.close()
            return results

    @staticmethod
    def filter_infected(param, value):
        connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', cursorclass=pymysql.cursors.DictCursor)
        query = f"SELECT ID, NAME, GRAVEYARD, CITY FROM INFECTED WHERE {param} = '{value}'"

        with connection:
            cursor = connection.cursor()
            cursor.execute(query)
            results = list(cursor.fetchall())

            cursor.close()
            return results

    @staticmethod
    def select_infected_info(id):
        connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', cursorclass=pymysql.cursors.DictCursor)

        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ID, NAME, GRAVEYARD, CITY FROM INFECTED WHERE ID=%s", id)
            results = list(cursor.fetchall())

            cursor.close()
            return results

    @staticmethod
    def insert_infected(name, graveyard, city):
        connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', cursorclass=pymysql.cursors.DictCursor)

        with connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO INFECTED(NAME, GRAVEYARD, CITY) VALUES(%s, %s, %s)", (name, graveyard, city))
            connection.commit()
            cursor.close()

    @staticmethod
    def update_infected(id, graveyard, city):
        connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', cursorclass=pymysql.cursors.DictCursor)

        with connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE INFECTED SET GRAVEYARD=%s, CITY=%s WHERE ID=%s", (graveyard, city, id))
            connection.commit()
            cursor.close()

    @staticmethod
    def delete_infected(id):
        connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', cursorclass=pymysql.cursors.DictCursor)

        with connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM INFECTED WHERE ID=%s", id)

            connection.commit()
            cursor.close()
