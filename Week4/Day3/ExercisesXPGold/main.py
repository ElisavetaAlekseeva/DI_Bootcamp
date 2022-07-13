# Exercise 1: Birthday Look-Up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user

# birthdays = {
#     'lisa': '23/11/1',
#     'sasha': '19/1/99',
#     'masha': '4/4/2',
#     'andrew': '5/1/4',
#     'kate': '27/9/98'
# }
# print('You can look up the birthdays of the people in the list!')
# users_answer = input('enter persons name ')
# if users_answer in birthdays.keys():
#     print(birthdays[users_answer])



# Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)
# birthdays = {
#     'lisa': '23/11/1',
#     'sasha': '19/1/99',
#     'masha': '4/4/2',
#     'andrew': '5/1/4',
#     'kate': '27/9/98'
# }
# print('You can look up the birthdays of the people in the list!')
# print(list(birthdays.keys()))
# users_answer = input('enter persons name ')
# if users_answer in birthdays.keys():
#     print(birthdays[users_answer])
# if users_answer  not in birthdays.keys():
#     print(f'Sorry, we don’t have the birthday information for {users_answer}')


# Exercise 3: Add Your Own Birthday
# Instructions
# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.
# birthdays = {
#     'lisa': '23/11/1',
#     'sasha': '19/1/99',
#     'masha': '4/4/2',
#     'andrew': '5/1/4',
#     'kate': '27/9/98'
# }
# print('You can look up the birthdays of the people in the list!')
# print(list(birthdays.keys()))
# users_persons_name = input('enter a name: ')
# users_birthday = input('enter his birthday(in the format “YYYY/MM/DD”): ')
# new_person = {users_persons_name: users_birthday}
# birthdays.update(new_person)
# users_answer = input('enter persons name  ')
# if users_answer in birthdays.keys():
#     print(birthdays[users_answer])
# if users_answer  not in birthdays.keys():
#     print(f'Sorry, we don’t have the birthday information for {users_answer}')




# Exercise 4: Fruit Shop
# Instructions
# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
# items = {
#     "banana": {"price": 4 , "stock":10},
#     "apple": {"price": 2, "stock":5},
#     "orange": {"price": 1.5 , "stock":24},
#     "pear": {"price": 3 , "stock":1}
# }
# 1
# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# empty_str = 'in our store we have: '
# for item, price in items.items():
#     empty_str += (f"{item} - {price} ")
# print(empty_str)

# 2
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
sum = 0
# print(items["banana"]['stock'])
for item in items.keys():
    price = items[item]['price']
    stock = items[item]['stock']
    sum += price * stock
print(sum)