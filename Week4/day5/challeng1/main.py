# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.
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
    for i in list:
        i = i ** 2
        
    print(list)
norm([1,2,2])