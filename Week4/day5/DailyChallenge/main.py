
# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world


users_input = 'without,hello,bag,world'
users_input_list = users_input.split(',')
sorted_users_input_list = sorted(users_input_list)
sorted_users_input = ','.join(sorted_users_input_list)
print(sorted_users_input)