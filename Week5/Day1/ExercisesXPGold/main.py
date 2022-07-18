# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.
import math
from random import randint


class Circle:
    def __init__(self, radius = 1.0) -> None:
        self.radius = radius
    def compute_perimetr (self, radius):
        perimeter = 2 * math.pi * radius
        return perimeter
    def compute_area (self, radius):
        area = radius ** 2 * math.pi 
        return area
    def geometrical_definition(self):
        print(self.compute_perimetr(self.radius))
        print(self.compute_area(self.radius))

circle = Circle(10)
circle.geometrical_definition()




# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
class MyList:
    def __init__(self, letters) -> None:
        self.letters = letters
    def reversed_list(self):
        return self.letters[::-1]

    def sorted_list(self):
        return sorted(self.letters)

    def create_random_list(self):
        random_list = []
        for i in range(len(self.letters)):
            random_num = randint(0,9)
            random_list.append(random_num)
        return(random_list)
        
blablabla = MyList ('mamapapaya')
print(blablabla.sorted_list())
print(blablabla.reversed_list())
print(blablabla.create_random_list())





# Exercise 3 : Restaurant Menu Manager
# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.
# Create a python file called menu_manager.py.
# Create a class called MenuManager.
# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).
# Here is a list of the dishes currently on the menu:
#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True
#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy
# The dishes provided above should be the value of the menu attribute.
# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.
# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.
# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.
# menu = {}

class Dish:
    def __init__(self, name, price, spice, gluten):
        self.name = name
        self.price = price
        self.spice = spice
        self.gluten = gluten

    def __str__(self):
        return(f'Name: {self.name} - {self.price} - {self.spice} - {self.gluten}')

class MenuManager:

    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        self.menu.append(Dish(name, price, spice, gluten))

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish.name == name:
                dish.price = price
                dish.spice = spice
                dish.gluten = gluten
            else:
                print(f'{name} is not in menu')

    def remove_item(self, name):
        for dish in self.menu:
            if dish.name == name:
                self.menu.remove(dish)
            else:
                print(f'{name} is not in menu')

    def show(self):
        for dish in self.menu:
            print(str(dish))


menu = MenuManager()

menu.add_item('soup', 10, 'B', True)
menu.show()
menu.update_item('soup', 15, 'C', False)
menu.add_item('pizza', 17, 'B', True)
menu.show()
menu.remove_item('soup')
menu.show()

