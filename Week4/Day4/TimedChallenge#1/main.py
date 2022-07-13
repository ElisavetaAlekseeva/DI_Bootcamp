# Count Occurence
# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.

string = input('enter a string: ')
letter = input('enter a letter: ')
sum = 0
for i in string:
    if letter in i:
        sum += 1
print(sum)