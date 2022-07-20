# Instructions :
# Consider this list
# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.
import translators as ts


french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translate_list = []
for word in french_words:
    translate_list.append(ts.google(word, from_language='fr'))

translate_dict = dict(zip(french_words, translate_list))
print(translate_dict)


