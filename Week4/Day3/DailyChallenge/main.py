# Instructions
# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples
# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }
# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}
# users_word = input('enter a word: ')
# dictn = {}
# for i, letter in enumerate(users_word):
#     if letter not in dictn:
#         dictn[letter] = []
#         dictn[letter].append(i)
#     elif letter in dictn:
#         dictn[letter].append(i)
# print(dictn)




# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

money_in_wallet = int(input('How much money do you have in your wallet: '))
can_afford = []      
cant_afford = []
for key, price in items_purchase.items():
    money = price.replace(price[0], '')
    if int(money) <= money_in_wallet:
        can_afford.append(key)
    else:
        cant_afford.append(price)

if len(cant_afford) == len(items_purchase):
    print('nothing')
else:
    print(sorted(can_afford))



