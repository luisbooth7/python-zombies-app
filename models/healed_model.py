import pymysql.cursors


class Healed:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select_healed():
        connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', cursorclass=pymysql.cursors.DictCursor)

        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT NAME FROM HEALED")
            results = list(cursor.fetchall())

            cursor.close()
            return results

    @staticmethod
    def insert_healed(name):
        connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', cursorclass=pymysql.cursors.DictCursor)

        with connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO HEALED (NAME) VALUES(%s)", name)
            connection.commit()
            cursor.close()
