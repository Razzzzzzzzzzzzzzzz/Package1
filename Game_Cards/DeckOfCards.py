from Game_Cards.Card import Card
from random import shuffle, randint

class DeckOfCards:
    def __init__(self):
        """Creates a cards deck of 52 unique cards."""
        self.cards = []
        for card_value in range(1,14):
            for card_symbol in range(1,5):
                self.cards.append(Card(card_value,card_symbol)) # Adds the value&symbol to the card

    def __str__(self):
        """Creates a string out of the list of cards and returns it."""
        cards_deck = f"-----[Cards Deck - {len(self.cards)} Cards]-----\n"
        for i in self.cards:
            cards_deck += f"{i} " # Prints the cards in the cards deck
        return cards_deck

    def __repr__(self):
        """Creates a string out of the list of cards and returns it."""
        cards_deck = f"-----[Cards Deck - {len(self.cards)} Cards]-----\n"
        for i in self.cards:
            cards_deck += f"{i} " # Prints the cards in the cards deck
        return cards_deck

    def cards_shuffle(self):
        """Re-order the cards in a random order."""
        if len(self.cards) > 0: # If the cards deck holds at least one card
            shuffle(self.cards)

    def deal_one(self):
        """Returns a random card from the cards deck list after removing it."""
        if len(self.cards) > 0:
            return self.cards.pop(randint(0,len(self.cards)-1)) # pops a random card from the list and returns it.