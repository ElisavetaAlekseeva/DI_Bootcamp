# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.
# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.


# def abs(value):
#     """The abs() function returns the absolute value of the given number."""

# def int():
#     """The int() function converts the specified value into an integer number."""

# def input():
#     """Python input() function is used to take user input"""

# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)





#  Exercise 2: Currencies
# Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     #Your code starts HERE
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)
# >>> str(c1)
# '5 dollars'
# >>> int(c1)
# 5
# >>> repr(c1)
# '5 dollars'
# >>> c1 + 5
# 10
# >>> c1 + c2
# 15
# >>> c1 
# 5 dollars
# >>> c1 += 5
# >>> c1
# 10 dollars
# >>> c1 += c2
# >>> c1
# 20 dollars
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

from ast import Num
import numbers


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        output = f"{self.amount} {self.currency}s"
        print (output)
        return output

    def __int__(self):
        return self.amount

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, number: int):
        if type(number) == int:
            sum = int(self) + number
            print(sum)
            return sum
        elif self.currency == number.currency:
            sum = int(self) + int(number)
        else:
            raise TypeError('Cannot add between Currency type <dollar> and <shekel>')


        print(self.amount + int(number))
        return self.amount + int(number)

    def __call__(self):
        print(f'{self.amount} {self.currency}s')
        return f'{self.amount} {self.currency}s'

    def __iadd__(self, number):
        self.amount += int(number)
        print(self.amount)
        return self




c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)
int(c1)
repr(c1)
c1 + 5
c1 + c2
c1()
c1 += 5
c1()
c1 += c2
c1()
c1 + c3