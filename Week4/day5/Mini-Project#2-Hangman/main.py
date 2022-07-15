# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.
import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
marked_word = ''
fails = 0
print(word)

def split(word):
    return [char for char in word]

def makeString(arr):
    string = ''
    for letter in arr:
        string += str(letter)
    return string

for letter in word:
    if letter == ' ':
        marked_word += ' '
    else:
        marked_word += '*'

word_list = split(word)
marked_word = split(marked_word)

while fails < 5 and makeString(marked_word) != word:
    users_guess = input('guess a letter: ')
    isNotFail = False
    while True:
        if users_guess in word_list:
            index = word_list.index(users_guess)
            marked_word[index] = users_guess
            word_list[index] = '*'
            isNotFail = True
        else:
            if not isNotFail:
                fails += 1
                print(f'{fails} try out of 5')
            if fails == 5:
                print('game over')
            break
        
    print(makeString(marked_word))

