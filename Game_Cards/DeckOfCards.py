from Card import Card
from random import shuffle, randint


class DeckOfCards:
    def __init__(self):
        self.cards = []
        for card_value in range(1,14):
            for card_symbol in range(1,5):
                self.cards.append(Card(card_value,card_symbol))

    def __str__(self):
        """Creates a string out of the list of cards and returns it."""
        cards_deck = "-----[Cards Deck]-----\n"
        for i in self.cards:
            cards_deck += f"{i} "
        cards_deck += f"\nCards remaining: {len(self.cards)}"
        return cards_deck

    def cards_shuffle(self):
        """Re-order the cards in a random order."""
        shuffle(self.cards)

    def deal_one(self):
        """Returns a random card from the cards deck list after removing it."""
        return self.cards.pop(randint(0,len(self.cards)-1)) # pops a random card from the list and returns it.

if __name__ == "__main__":
    game1 = DeckOfCards()
    print(game1)
    game1.cards_shuffle()
    print(game1)
    print(game1.deal_one())
    print(game1)