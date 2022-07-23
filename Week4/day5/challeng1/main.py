# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.
from array import array
import math


list_1 = {}
list_1[0] = 'first'
print(list_1)



# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.
string = 'Write a script that counts the number of spaces in a string'
spaces = 0
for i in string:
    if i == ' ':
        spaces += 1
print(spaces)



# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.
string_2 = 'WritE a script that calculates thE Number Of upper Case letters And lower case Letters in a string.'
lower_case = 0
upper_case = 0
for word in string_2:
    for letter in word:
        if letter.islower():
            lower_case += 1
        elif letter.isupper():
            upper_case += 1
print(upper_case)
print(lower_case)



# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:
#     >>>my_sum([1,5,4,2])
#     >>>12
def my_sum(array):
    sum = 0
    for i in array:
        sum += i
    print(sum)
my_sum([1,5,4,2])



# Exercise 5
# Instructions
# Write a function to find the max number in a list
#     >>>find_max([0,1,3,50])
#     >>>50
def find_max(array):
    largest_num = array[0]
    for i in array:
        if i > largest_num:
            largest_num = i
    print(largest_num)
find_max([0,51,3,50])




# Exercise 6
# Instructions
# Write a function that returns factorial of a number
#     >>>factorial(4)
#     >>>24
def factorial(num):
    factorial = num
    while num > 1:
        num -= 1
        factorial *= num
    print(factorial)
factorial(5)


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):
#     >>>list_count(['a','a','t','o'],'a')
#     >>>2
def list_count(list, letter):
    letters_count = 0
    for i in list:
        if i == letter:
            letters_count +=1
    print(letters_count)
list_count(['a','a','t','o'],'a')



# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
#     >>>norm([1,2,2])
#     >>>3
def norm(list):
    squaere_list = []
    sum = 0
    for i in list:
        i = i ** 2
        squaere_list.append(i)
    for i in squaere_list:
        sum += i
    square_root = math.sqrt(sum)
    print(square_root)

norm([1,2,2])





# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)
#     >>>is_mono([7,6,5,5,2,0])
#     >>>True
#     >>>is_mono([2,3,3,3])
#     >>>True
#     >>>is_mono([1,2,0,4])
#     >>>False

def is_mono(array):
    print (all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or
        all(array[i] >= array[i + 1] for i in range(len(array) - 1)))

is_mono([7,6,5,5,2,0])
is_mono([2,3,3,3])
is_mono([1,2,0,4])


# def is_mono(array):
#     return (all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or
#             all(array[i] >= array[i + 1] for i in range(len(array) - 1)))

# is_mono([7,6,5,5,2,0])
# is_mono([2,3,3,3])
# is_mono([1,2,0,4])


# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.
def longest_word(array):
    max_len = max(array, key=len)
    print(max_len)
longest_word(['bubble', 'tea', 'home', 'polindrome'])



# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
def separate(array):
    int_list = []
    str_list = []
    for i in array:
        if type(i) == int:
            int_list.append(i)
        else:
            str_list.append(i)
    print(int_list)
    print(str_list)
separate(['mama', 1, 3, 4, 'summer', 7, 'python'])





# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:
#     >>>is_palindrome('radar')
#     >>>True
#     >>>is_palindrome('John)
#     >>>False
def is_palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        print(True)
    else:
        print(False)
is_palindrome('radar')
is_palindrome('John')



# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:
#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3


def sum_over_k(sentence,k):
    amount = 0
    sentence_list = sentence.split()
    for word in sentence_list:
        if len(word) > k:
            amount += 1
    print(amount)

sentence = 'Do or do not there is no try'
k=2
sum_over_k(sentence,k)




# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):
#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3

def dict_avg (dict):
    sum = 0
    for val in dict.values():
        sum += val
    average = sum / len(dict)
    print(average)

dict_avg({'a': 1,'b':2,'c':8,'d': 1})





# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:
#     >>>common_div(10,20)
#     >>>[2,5,10]

def common_div (num1, num2):
    min_number = min([num1, num2])
    common_divisors = []
    for i in range(1,min_number + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
    print(common_divisors)

common_div(10,20)




# Exercise 16
# Instructions
# Write a function that test if a number is prime:
#     >>>is_prime(11)
#     >>>True
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False 
    return True
print(is_prime(11))




# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:
#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]



def weird_print(array):
    even_list = []
    for index, number in enumerate(array):
        if index % 2 == 0 and number % 2 == 0:
            even_list.append(number)
    print(even_list)
weird_print([1,2,2,3,4,5,6,6,6])




# Exercise 18
# Instruction
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:
#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2

def type_count (**kwargs):
    # type_dict = {'int': 0, 'str': 0, 'float': 0, 'bool':0}
    type_dict = {}
    for value in kwargs.values():
        for k, v in type_dict.items():
            if k in type_dict.keys():
                type_dict[k] += 1
            else:
                type_dict[type(value)] = 1
    print(type_dict)
type_count(a = 1 ,b='string',c=1.0,d=True,e=False)




# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings. 
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.
def split_str(string, splitter = ' '):
    result = []
    temp = ''
    for letter in string:
        if letter != splitter:
            temp += letter
        else:
            result.append(temp)
            temp = ''
    result.append(temp)
    print(result)
split_str('kate,and, ron', ',')




# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"
users_input = input('Enter your password: ')
password = ''
for letter in users_input:
    password += '*'
print(password)