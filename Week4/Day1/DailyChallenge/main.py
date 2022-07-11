# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# Then, print the first and last characters of the given text.
# Using a for loop, construct the string character by character:asdfghjklo
#  Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World
# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
# Hlrolelwod

#1
from email import message
from math import radians
from random import random, shuffle


user_string = str(input('enter a string.The string must be 10 characters long '))
if len(user_string) < 10:
    print('string not long enough')
elif len(user_string) > 10:
    print('string too long')
    
#2
print(user_string[0])
print(user_string[len(user_string)-1])

#3
string = 'Hello world'
empty = ''
for x in string:
    empty+=x
    print(empty)

#4
import random
shuffleString= ''.join(random.sample(string, len(string)))
print(shuffleString)