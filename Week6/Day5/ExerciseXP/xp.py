# PART 1
# In this exercise we will use PostgreSQL and Python. Create a new database and a new table in pgAdmin (or in psql). Read the instructions below before creating the new table
# Create a new class called MenuItem, the attributes should be the name and price of each item.
# Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the database.
# Within the MenuItem class create a method called all which will return a list of all our MenuItem objects.
# Create another method called get_by_name that will return a single MenuItem object depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.




import psycopg2
import re 

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'password'
DATABASE = 'database'

def run_query(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        results = cursor.fetchall()
        connection.close()
        return results
    except:
        connection.close()

class MenuItem():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def save(self):
        insert_query = f"insert into menu (name, price) values ('{self.name}', {self.price})"
        run_query(insert_query)

    @classmethod
    def delete(name):
        query = f'delete from menu where name = "{name}"'
        run_query(query)

    def update(self, name, price):
        query = f'update menu set price = {price}, set name = "{name}" where name = "{self.name}"'
        run_query(query)
        
    @classmethod
    def all():
        query = f'select * from menu'
        run_query(query)

    @classmethod
    def get_by_name(name):
        query = f'select * from menu where name = "{name}"'
        run_query(query)

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all()