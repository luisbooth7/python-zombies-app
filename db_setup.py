import pymysql.cursors
from models.infected_model import Infected
from models.healed_model import Healed

if __name__ == '__main__':
    connection = pymysql.connect(host='localhost', user='root', passwd='root', db='ph', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS INFECTED(ID INT NOT NULL AUTO_INCREMENT, NAME VARCHAR(255) NOT NULL, GRAVEYARD VARCHAR(255) NOT NULL, PRIMARY KEY (ID), CITY VARCHAR(255) NOT NULL)")

connection.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS HEALED(ID INT NOT NULL AUTO_INCREMENT, NAME VARCHAR(255) NOT NULL, PRIMARY KEY (ID))")

connection.commit()

cursor.close()
connection.close()

Infected.insert_infected('Liquid Ocelot', 'Outer Haven', 'Raccoon City')
Infected.insert_infected('Reinhardt', 'Greyfriars Kirkyard', 'Eichenwalde')
Infected.insert_infected('John Marston','Blackwater Cemetery', 'Armadillo')
Healed.insert_healed("Chris Redfield")
