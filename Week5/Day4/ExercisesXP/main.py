# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# Download this word list
# Save it in your development directory.
# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
# Take the random words and create a sentence (using a python method), the sentence should be lower case.
# Create a function called main which will:
# Print a message explaining what the program does.
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
from random import randint, sample
import requests

def get_words_from_file(file):
    with open(file, mode = 'r') as f:
        words_list = []
        for word in f:
            words_list += word.split()
        return words_list

print(get_words_from_file('sample.txt'))


def get_random_sentence(length):
    word_list = get_words_from_file('sample.txt')
    sentence = ''
    str_length = 0
    while str_length < length:
        random_index = word_list[randint(0, len(word_list)-1)]
        sentence += ' ' + random_index
        str_length += 1
    return sentence
# get_random_sentence(5)


def main():
    print('This program takes the random words and create a sentence, the sentence should be lower case')
    sentence_length = int(input('Sentence length: '))
    if 2 < sentence_length < 20:
        random_sentence = str(get_random_sentence(sentence_length))
        print(random_sentence.lower())

main()






# Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.



import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
salary = data['company']['employee']['payable']['salary']
print(salary)

data['company']['employee']['birth_date'] = '23/11'
with open('sampleJson.json', 'w') as f:
    json.dump(data, f)
   

print(sampleJson)