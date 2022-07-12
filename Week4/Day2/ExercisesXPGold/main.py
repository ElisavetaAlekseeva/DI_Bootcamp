# Exercise 1: Concatenate Lists
# Instruction
# Write code that concatenates two lists together without using the + sign.
from tkinter import W


first_list = [1,2,3,4,5]
second_list = [6,7,8,9]
first_list.extend(second_list)
print(first_list)


# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range(1499, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


# Exercise 3: Check The Index
# Instructions
# Using this variable
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input('enter your name: ')
if user_name in names:
    print(names.index(user_name))



# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87
#     The greatest number is: 87
user_first_number = int(input('enter 1st number '))
user_second_number = int(input('enter 2nd number '))
user_third_number = int(input('enter 3rd number '))
print(max([user_first_number, user_second_number, user_third_number]))



# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowel = 'aeiouy'
for i in alphabet:
    if i in vowel:
        print(f'{i} is a vowel ')
    else:
        print(f'{i} is a consonant ')



# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
words = input('enter 7 words: ').split(' ')
letter = input('enter a single character: ')
for i in words:
    if letter in i:
        print(f'in {i} index of letter {letter} is: {i.index(letter)}')
    else:
        print(f'sorry, letter {letter} doesnt exist in {i}')





# Exercise 7:
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
from_one_to_million = []
for i in range(0, 1000001,1):
    from_one_to_million.append(i)
print(min(from_one_to_million))
print(max(from_one_to_million))
print(sum(from_one_to_million))




# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
users_number = input('enter equence of comma-separated numbers: ')
print(users_number.split(','))
print(tuple(users_number.split(',')))



# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost
import random
user_input = int(input('input a number from 1 to 9 (including): '))
random_number = random.randint(1,10)
games_won = 0
games_lost = 0
while user_input != random_number:
    print('better luck next time.')
    random_number = random.randint(1,10)
    games_lost += 1
    user_input = int(input('input a number from 1 to 9 (including): '))
if user_input == random_number:
    print('WINNER')
    games_won += 1


