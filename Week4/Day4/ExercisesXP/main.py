# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
from math import degrees
from random import random


def display_message():
    return f'i learned: functions, args, kwargs'
print(display_message())



# Exercise 2: What’s Your Favorite Book ?
# Instruction
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.
def favorite_book(title):
    return f'One of my favorite books is {title}'
print(favorite_book('Alice in Wonderland'))




# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>". 
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city (city = 'SPb', country = 'Russia'):
    return f'{city} is in {country}'
print(describe_city())



# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
import random
# def compare_numbers(number):
#     random_number = random.randint(0,100)
#     if number == random_number:
#         return 'success'
#     else:
#         return f'fail {number} {random_number}'
# print(compare_numbers(54))
random_number = random.randint(0,100)
compare_numbers = lambda number: 'success' if number == random_number else  f'fail {number} {random_number}'
print(compare_numbers(8))



# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message. 
# Bonus: Call the function make_shirt() using keyword arguments.
def make_shirt(size='large', text='I love Python'):
    print (f'The size of the shirt is {size} and the text is {text}')    
make_shirt()





#  Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for name in magician_names:
        print(name)
show_magicians()
def make_great ():
    for name in magician_names:
        print(f"The Great {name}")
make_great()










# Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
def get_random_temp (season = 'autumn'):
    if season == 'winter':
        random_degrees = random.randint(-10,6)
    if season == 'spring' or season == 'autumn'or season == 'fall':
        random_degrees = random.randint(7,25)
    if season == 'summer':
        random_degrees = random.randint(25,40)
    return random_degrees
# print(get_random_temp())

def season():
    users_month = int(input('enter a number of the month '))
    if 1 <= users_month <= 2 or users_month == 12:
        return 'winter'
    elif 3 <= users_month <= 5:
        return 'spring'
    elif 9 <= users_month <= 11:
        return 'autumn'
    elif 6 <= users_month <= 8:
        return 'summer'

def main():
    users_season = season()
    degrees = int(get_random_temp(users_season))
    print(f'The temperature right now is {degrees} degrees Celsius')
    if degrees < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0 <= degrees <= 16:
        print('Quite chilly! Don’t forget your coat')
    elif 16 < degrees <= 24:
        print('nice weather')
    elif 24 < degrees <= 32:
        print('too hot')
    elif 32 < degrees <= 40:
        print('too hot, stau home')
    
main()


