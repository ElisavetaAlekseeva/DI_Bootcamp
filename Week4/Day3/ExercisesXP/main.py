# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = list(zip(keys, values))
print(dictionary)


# Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Given the following object:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for age in family.values():
    if 3 <= age <= 12:
        total_cost += 10
    elif age > 12:
        total_cost += 15
print(total_cost)




# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US. 
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000
brand = {
    'name': 'Zara',
    'creation_date': 1975 ,
    'creator_name': {'Amancio', 'Ortega' ,'Gaona'} ,
    'type_of_clothes': {'men', 'women', 'children', 'home'} ,
    'international_competitors': ['Gap', 'H&M', 'Benetton'] ,
    'number_stores': 7000 ,
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': {'pink', 'green'}
    }
}
# 3
brand['number_stores'] = 2
print(brand['number_stores'])

# 4
types = brand['type_of_clothes']
sentence = 'we have clothers for: '
for i in types:
    sentence += i+' '
print(sentence)

# 5
brand['country_creation'] = 'spain'

# 6
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
# 7
brand.pop('creation_date')
# 8
print(brand['international_competitors'][-1])
# 9
print(brand['major_color']['US'])
# 10
print(len(brand))
# 11
print(brand.keys())
# 12,13
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
brand.update(more_on_zara)
print(brand)
# 14
print(brand['number_stores'])







# Exercise 4 : Disney Characters
# Instructions
# Use this list :
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
# #1/
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# #2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# #3/ 
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_A = {}
# for i in users:
#     disney_users_A[i] = users.index(i)
# print(disney_users_A)

# disney_users_B = {}
# for i in users:
#     disney_users_B[users.index(i)] = i
# print(disney_users_B)

# disney_users_C = sorted(disney_users_A.items())
# print(sorted(disney_users_C))
# 4.1
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_A = {}
# for i in users:
#     if 'i' in i:
#         disney_users_A[i] = users.index(i)
# print(disney_users_A)
# 4.2
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
for i in users:
    for x in i:
        if x[0] == 'M' or x[0] == 'P':
            disney_users_A[i] = users.index(i)
print(disney_users_A)