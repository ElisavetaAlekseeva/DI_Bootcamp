# 🌟 Exercise 1: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:
# import module_name 
# OR 
# from module_name import function_name 
# OR 
# from module_name import function_name as fn 
# OR
# import module_name as mn



# Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

from datetime import datetime , timedelta
from datetime import date
from random import randint
import string
import random
from datetime import date
from faker import Faker



def accepts_number(number:int) -> str:
    random_number = randint(0,101)
    if number == random_number:
        print('display a success message to the user')



# Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
random_string = ''.join(random.choices(string.ascii_letters, k = 5))
print(random_string)



# 🌟Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.
def current_date():
    x = date.today()
    print(x)
current_date()


# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).
def until_january():
    today = datetime.now()
    january_1st = datetime(2023, 1 , 1, 00, 00, 00)
    print(january_1st - today)
until_january()

# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
# def minutes_you_lived():
#     birthdate = datetime(2001, 11 , 23, 00, 00, 00)
#     today = datetime.now()
#     # difference = today - birthdate
#     # minuts = days * 24 * 60
#     difference = birthdate + datetime.timedelta(today)
#     return difference
# # minutes_you_lived(datetime(2001, 11 , 23, 00, 00, 00))
# print(minutes_you_lived())

def minutes_you_lived(birthdate):
    today = datetime.now()
    difference = today - birthdate
    difference_in_sec = difference.total_seconds
    minutes = divmod(difference_in_sec(), 60)[0]
    print('minutes')
    return(minutes)

print(minutes_you_lived(datetime(2001, 11 , 23, 00, 00, 00)))



# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

def untill_holidays():
    today = date.today()
    rosh_HaShanah = ('RoshHaShana',date(2022, 9,27))
    new_year = ('New Year',date(2023,1,1))
    independence_day = ('Independence day',date(2023,5,5))
    holidays_list = [rosh_HaShanah,new_year,independence_day]
    sorted_holidays = {}
    for holiday in holidays_list:
        until_holiday = holiday[1] - today
        sorted_holidays[holiday[0]] = until_holiday
    next_holiday = min(sorted_holidays.values())

    for key, val in sorted_holidays.items():
        if val == next_holiday: 
            print(f'the next holiday is {key} in {next_holiday} hours')
untill_holidays()




# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

class Age:
    def __init__(self, seconds:int) -> None:
        self.seconds = seconds
        self.one_year_on_earth = seconds/31557600

    def on_earth(self):
        return round(self.one_year_on_earth,2)
    def on_mercury(self):
        return round(self.one_year_on_earth / 0.2408467,2)
    def on_venus(self):
        return round(self.one_year_on_earth / 0.61519726,2)
    def on_mars(self):
        return round(self.one_year_on_earth / 1.8808158,2)
    def on_jupiter(self):
        return round(self.one_year_on_earth /  11.862615,2)
    def on_saturn(self):
        return round(self.one_year_on_earth /  29.447498,2)
    def on_uranus(self):
        return round(self.one_year_on_earth / 84.016846,2)
    def on_neptune(self):
        return round(self.one_year_on_earth / 164.79132,2)

lisa = Age(1000000000)
print(lisa.on_neptune())





# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.
fake = Faker()
users = []
def new_dictionaries():
    dictionarie_users = {'name': fake.name(),'adress': fake.address(),'langage code': fake.language_code() }
    users.append(dictionarie_users)
    print(dictionarie_users)
new_dictionaries()