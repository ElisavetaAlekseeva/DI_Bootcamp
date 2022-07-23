# instructions

# Part 1 : Quizz :

# Answer the following questions

# What is a class? Class is describing the structure of object
# What is an instance? instance is an object that belongs to class
# What is encapsulation? encapsulation is made from components that are only available within the class
# What is abstraction? abstraction is used to hide the internal functionality of the function from the users
# What is inheritance? inheritance allows to highlight the behavior common to several classes and take it into a separate entity
# What is multiple inheritance? the class capability has more than one parent class
# What is polymorphism? different behavior of the same method in different classes.
# What is method resolution order or MRO?it is the way in which the linearization of a class is composed




# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.
# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

from random import random, shuffle
import random


class Card:
    def cards(self):
        all_cards = []
        cards_value = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        cards_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for value in cards_value:
            for suit in cards_suit:
                card={}
                card[value] = suit
                all_cards.append(card)
        return all_cards


class Desk:
    def shuffle(self):
        cards = Card().cards()
        random.shuffle(cards)
        return cards

    def deal(self):
        shuffled_cards = self.shuffle()
        dealed_card = random.choice(shuffled_cards)
        shuffled_cards.remove(dealed_card)
        print(dealed_card)
        print(shuffled_cards)
a = Desk()
a.deal()