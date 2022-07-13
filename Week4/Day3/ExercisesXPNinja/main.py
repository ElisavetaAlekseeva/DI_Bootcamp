# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.
# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
from audioop import reverse
from enum import unique
string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
string_to_list= list(string.split(','))
print(f'in the list {len(string_to_list)} manufacturers/companies')
print(sorted(string_to_list, reverse=True))
count_of_o = 0
without_i = 0
for name in string_to_list:
    for letters in name:
        if 'o' in letters:
            count_of_o += 1
    if 'i' not in name:
        without_i += 1
print(count_of_o)
print(without_i)


names_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_names_list = set(names_list)
print(unique_names_list)
print(','.join(unique_names_list))
print(len(unique_names_list))


sorted_string_to_list = []
for name in string_to_list:
    new_name = sorted(name, reverse=True)
    sorted_string_to_list.append(''.join(new_name))
print(sorted(sorted_string_to_list))
