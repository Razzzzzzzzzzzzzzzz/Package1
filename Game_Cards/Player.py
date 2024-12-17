from Game_Cards.Card import Card
from Game_Cards.DeckOfCards import DeckOfCards
from random import randint

class Player:
    def __init__(self, name, cards_number = 26):
        if len(name) < 1:
            raise ValueError("Name can't be empty")
        if type(name) != str:
            raise TypeError("name must be a string!")
        self.name = name
        if 10 <= cards_number <= 26: # Checks for the cards number to be
                                             # within the allowed range.
            self.cards_number = cards_number
        else:
            self.cards_number = 26
        self.player_cards = []

    def __str__(self):
        return (f"-----[{self.name} - {len(self.player_cards)} Cards]-----\n"
                f"{self.player_cards}")

    def set_hand(self, cards_deck):
        """Gives the player a deck of cards according to the
         cards_number"""
        if type(cards_deck) != DeckOfCards:
            raise TypeError("Cards Deck must be a DeckOfCards Type!")
        if len(cards_deck.cards) >= self.cards_number: # if there are enough
                                                   # cards in the cards deck
            for card in range(self.cards_number):
                added_card = cards_deck.deal_one()
                print(added_card)
                self.player_cards.append(added_card) # adds a card
                                          # from the cards deck to the player

    def get_card(self):
        """The method takes one random card from the player"""
        if len(self.player_cards) > 0:
            return self.player_cards.pop(randint(0, len(self.player_cards)
                                                 - 1))

    def add_card(self, new_card):
        """Method that adds a card to the user"""
        if type(new_card) == Card:
            self.player_cards.append(new_card)