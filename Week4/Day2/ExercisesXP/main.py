# Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# from ast import And, Not


# my_fav_numbers = {3,7,20,33}
# more_numbers = {45, 99}
# my_fav_numbers.update(more_numbers)
# print(my_fav_numbers)
# my_fav_numbers.pop()
# print(my_fav_numbers)
# friend_fav_numbers = {64, 78, 81}
# print(friend_fav_numbers)
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)


# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
#no


# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0, 'Apples')
# basket.count('Apples')
# print(basket.count('Apples'))
# basket.clear()
# print(basket)


# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# an integer is a whole number
# a float  its a number with a decimal point

# new_list = []
# num = 1.5
# new_list.append(num)
# for i in range(2,6):
#     decimal = i + 0.5
#     new_list.append(i)
#     new_list.append(decimal)
# print(new_list)


# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# for i in range (1,21):
#     if i % 2 == 0:
#         print(i)


# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# user = input('enter your name ')
# while user != 'Lisa':
#     user = input('enter your name ')



# Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits). 
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# user_fruit = input('Enter your favorite fruits ')
# fruits = user_fruit.split(' ')
# print(fruits)
# users_fav_fruit = input('Enter one favorite fruit ')
# if users_fav_fruit in fruits:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy')



# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
# 1
# users_top = input(' enter a pizza toppings ')
# print(f' you added {users_top} topping to their pizza.')
# price = 12.5
# all_toppings = []
# all_toppings.append(users_top)
# while users_top != 'quit':
#     users_top = input(' enter a pizza toppings ')
#     print(f' you added {users_top} topping to their pizza.')
#     price += 2.5
#     all_toppings.append(users_top)
#     if users_top == 'quit':
#         price += 2.5
#         print(f'price is: {price}')
#         print(f'the list of your toppings is: {all_toppings}')
#         break


# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

# from stat import IO_REPARSE_TAG_APPEXECLINK


# family_ages = input('enter the age of each person who wants a ticket: ').split(',')
# sum = 0
# print(family_ages)
# for x in family_ages:
#     if (3 <= int(x)) & (int(x) <= 12):
#         sum += 10
#     elif int(x) > 12:
#         sum += 15
# print(sum)



# names_list = ['lisa', 'masha', 'sasha', 'kate']
# ages_list = []

# for i in names_list:
#     ages_list.append(input(f'enter age of {i}: '))

# remove_list = []

# for x in ages_list:
#     if 15 < int(x) and int(x) < 22:
#         print('ok')
#     else:
#         remove_list.append(names_list[ages_list.index(x)])

# for i in remove_list:
#     names_list.pop(names_list.index(i))

# print(names_list)
        

# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.


# sandwich_orders = ["Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwiches = []
# for i in sandwich_orders:
#     asking_is_sandwich_done = input(f'enter \'yes\' if {i} is made or \'not\' if it  isnt ')
#     if asking_is_sandwich_done == 'yes':
#         finished_sandwiches.append(i)
# if len(finished_sandwiches) == len(sandwich_orders):
#     for i in finished_sandwiches:
#         print(f'I made your {i} ')



# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
# sandwich_orders = ["Avocado sandwich","Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich"]
# print('the deli has run out of pastrami,sorry ')
# finished_sandwiches = []
# for i in sandwich_orders:
#         finished_sandwiches.append(i)
# while 'Pastrami sandwich' in finished_sandwiches:
#     finished_sandwiches.remove('Pastrami sandwich')
# print(finished_sandwiches)