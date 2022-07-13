# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula: 
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:
# 18,22,24
from enum import unique
import math
from os import remove
# a = math.sqrt(49)

users_numbers = input('enter a comma-separated string of numbers: ').split(',')
c = 50
h = 30
for (i)in users_numbers:
    d = int(i)
    formula = (2 * c * d / h)
    q = math.sqrt(formula)
    print(q)




# Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# Store the list of numbers in a variable.
# Print the following information: 
# a. The list of numbers – printed in a single line 
# b. The list of numbers – sorted in descending order (largest to smallest) 
# c. The sum of all the numbers
# A list containing the first and the last numbers.
# A list of all the numbers greater than 50.
# A list of all the numbers smaller than 10.
# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# The numbers without any duplicates – also print how many numbers are in the new list.
# The average of all the numbers.
# The largest number.
# 10.The smallest number.
# 11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
# 12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier. 
# 13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
# 14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# 15.Bonus: Will the code work when the number of random numbers is not equal to 10?
# 1
list_of_numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
# 2
print(list_of_numbers)
list_of_numbers.sort(reverse=True)
print(list_of_numbers)
print(sum(list_of_numbers))
# 3
first_and_last = []
first_and_last.append(list_of_numbers[0])
first_and_last.append(list_of_numbers[-1])
print(first_and_last)
# 4
greater_than_50 = []
for i in list_of_numbers:
    if i > 50:
        greater_than_50.append(i)
print(greater_than_50)
# 5
smaller_than_10 = []
for i in list_of_numbers:
    if i < 10:
        smaller_than_10.append(i)
print(smaller_than_10)
# 6
numbers_squared = []
for i in list_of_numbers:
    new_i = i ** 2
    numbers_squared.append(new_i)
print(numbers_squared)
# 7
# 8
average = sum(list_of_numbers) / len(list_of_numbers)
print(average)
# 9,10
print(min(list_of_numbers))
print(max(list_of_numbers))




# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.
paragraph = 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for lorem ipsum will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'
4
characters_in_paragraph = len(paragraph)
print(characters_in_paragraph)
# 5
sentences_in_paragraph = paragraph.split('.')
print(len(sentences_in_paragraph))
# 6
words_in_paragraph = paragraph.split(' ')
print(len(words_in_paragraph))
7
paragraph_splt = paragraph.split()
for i, word in enumerate(paragraph_splt):
    word = word.strip('.')
    paragraph_splt[i] = word
print(len(set(paragraph_splt)))





# Exercise 4
# Instructions
# Write a program that prints the frequency of the words from the input.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1

