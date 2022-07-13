# users_string = input('Enter a string: ')
users_string = 'You have entered a wrong domain'
reversed_list = users_string.split()[::-1]
reversed_string = ' '.join(reversed_list)

print(reversed_string)